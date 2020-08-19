import math
from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required
from sqlalchemy.orm.exc import NoResultFound
from api.extensions import guard
from api.models.user import User
from api.utils import get_cosine, get_euc, get_doc_ids, Tfidf

users = Blueprint('users', __name__)

# initialise global for tfidf
id_list = None
user_tfidf = None


def generate_user_corpus(user):
    string = ''
    for item in user[1:]:  # skip id
        string += (str(item) + " - ")
    return string


def get_user_matches(query, doc_id):
    user_list = []
    for item in get_doc_ids(query, id_list, 10, doc_id):

        # can't minimise to comprehension yet, get 'corrupted double-linked list' error
        data = {}
        user = User.query.filter_by(id=item).one_or_none()
        for key in user.__table__.columns.keys():
            data[key] = eval('user.' + key)
        user_list.append(data)

    return user_list


def get_jobs_based_on_users(query, doc_id):
    application_list = []
    for item in get_doc_ids(query, id_list, 10, doc_id):
        for job in User.query.filter_by(id=item).one_or_none().applications:
            application_list.append(job.as_dict())
    return application_list


@users.before_app_first_request
def load_global_data():
    global id_list
    global user_tfidf

    query = User.query.with_entities(User.id, User.degree_type, User.major, User.work_history_count,
                                     User.work_history_years_experience, User.employed, User.managed_others,
                                     User.managed_how_many) \
        .filter_by(role='candidate').order_by(User.id.asc()).all()

    id_list = [r[0] for r in query]

    text_data = []
    for user in query:
        text_data.append(generate_user_corpus(user)[:-3])  # remove ' - ' at the end of the string

    user_tfidf = Tfidf(text_data)


@users.route('/users/all', methods=['GET'])
@auth_required
def users_all():
    query = User.query.order_by(User.id.asc())
    if 'page' in request.args:
        page = int(request.args['page'])
        return jsonify({'total': math.ceil(query.paginate(page, 10, False).total / 10), 'users': [user.as_dict() for user in query.paginate(page, 10, False).items]})
    else:
        return jsonify({'total': math.ceil(query.paginate(1, 10, False).total / 10), 'users': [user.as_dict() for user in query.paginate(1, 10, False).items]})


@users.route('/users/<user_id>', methods=['GET'])
@auth_required
def get_user(user_id):
    if user_id:
        try:
            return jsonify(User.query.filter_by(id=user_id).one().as_dict())
        except NoResultFound:
            return "No result found"
    else:
        return "Error: No id field provided. Please specify an id."


@users.route('/me', methods=['GET'])
@auth_required
def get_profile_from_token():
    token = guard.read_token_from_header()
    user = User.query.filter_by(id=guard.extract_jwt_token(token)['id']).one()
    return jsonify(user.as_dict())


@users.route('/users/my_applications', methods=['GET'])
@auth_required
def get_applications():
    token = guard.read_token_from_header()
    applications = User.query.filter_by(id=guard.extract_jwt_token(token)['id']).one().applications
    return jsonify([job.as_dict() for job in applications])


@users.route('/users/matching/<sim_type>', methods=['GET'])
@auth_required
def matching_jobs(sim_type):
    token = guard.read_token_from_header()
    user = User.query.with_entities(User.id, User.degree_type, User.major, User.work_history_count,
                                    User.work_history_years_experience, User.employed, User.managed_others,
                                    User.managed_how_many).filter_by(id=guard.extract_jwt_token(token)['id']).one()
    if sim_type == 'cosine':
        return jsonify(get_user_matches(get_cosine(user_tfidf.vectorizer, user_tfidf.weights, generate_user_corpus(user)), user.id))
    elif sim_type == 'euclidean':
        return jsonify(get_user_matches(get_euc(user_tfidf.vectorizer, user_tfidf.weights, generate_user_corpus(user)), user.id))


@users.route('/users/my_applications/matching/<sim_type>/', methods=['GET'])
@auth_required
def matching_applications(sim_type):
    token = guard.read_token_from_header()
    user = User.query.with_entities(User.id, User.degree_type, User.major, User.work_history_count,
                                    User.work_history_years_experience, User.employed, User.managed_others,
                                    User.managed_how_many).filter_by(id=guard.extract_jwt_token(token)['id']).one()
    if sim_type == 'cosine':
        return jsonify(get_jobs_based_on_users(get_cosine(user_tfidf.vectorizer, user_tfidf.weights, generate_user_corpus(user)), user.id))
    elif sim_type == 'euclidean':
        return jsonify(get_jobs_based_on_users(get_euc(user_tfidf.vectorizer, user_tfidf.weights, generate_user_corpus(user)), user.id))
