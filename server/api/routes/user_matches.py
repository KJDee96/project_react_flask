from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required
from api.models.user import User
from api.utils import get_cosine, get_euc, get_doc_ids, Tfidf

user_matches = Blueprint('user_matches', __name__)

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


@user_matches.before_app_first_request
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


@user_matches.route('/cosine_users')
@auth_required
def cosine_users():
    json_data = request.get_json()
    user = User.query.with_entities(User.id, User.degree_type, User.major, User.work_history_count,
                                    User.work_history_years_experience, User.employed, User.managed_others,
                                    User.managed_how_many).filter_by(id=json_data['user_id']).one_or_none()

    return jsonify(get_user_matches(get_cosine(user_tfidf.vectorizer, user_tfidf.weights, generate_user_corpus(user)), user.id))


@user_matches.route('/euc_users')
@auth_required
def euc_users():
    json_data = request.get_json()
    user = User.query.with_entities(User.id, User.degree_type, User.major, User.work_history_count,
                                    User.work_history_years_experience, User.employed, User.managed_others,
                                    User.managed_how_many).filter_by(id=json_data['user_id']).one_or_none()

    return jsonify(get_user_matches(get_euc(user_tfidf.vectorizer, user_tfidf.weights, generate_user_corpus(user)), user.id))


@user_matches.route('/cosine_applications')
@auth_required
def cosine_applications():
    json_data = request.get_json()
    user = User.query.with_entities(User.id, User.degree_type, User.major, User.work_history_count,
                                    User.work_history_years_experience, User.employed, User.managed_others,
                                    User.managed_how_many).filter_by(id=json_data['user_id']).one_or_none()

    return jsonify(get_jobs_based_on_users(get_cosine(user_tfidf.vectorizer, user_tfidf.weights, generate_user_corpus(user)), user.id))


@user_matches.route('/euc_applications')
@auth_required
def euc_applications():
    json_data = request.get_json()
    user = User.query.with_entities(User.id, User.degree_type, User.major, User.work_history_count,
                                    User.work_history_years_experience, User.employed, User.managed_others,
                                    User.managed_how_many).filter_by(id=json_data['user_id']).one_or_none()

    return jsonify(get_jobs_based_on_users(get_euc(user_tfidf.vectorizer, user_tfidf.weights, generate_user_corpus(user)), user.id))
