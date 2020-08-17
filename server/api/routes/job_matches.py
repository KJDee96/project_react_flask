from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required
from api.models.job import Job
from api.utils import get_cosine, get_euc, get_doc_ids, Tfidf

job_matches = Blueprint('job_matches', __name__)

# initialise global for tfidf
id_list = None
job_tfidf = None


def get_matches(query, doc_id):
    job_list = []
    for item in get_doc_ids(query, id_list, 25, doc_id):

        # can't minimise to comprehension yet, get 'corrupted double-linked list' error
        data = {}
        job = Job.query.filter_by(id=item).one_or_none()
        for key in job.__table__.columns.keys():
            data[key] = eval('job.' + key)
        job_list.append(data)

    return job_list


@job_matches.before_app_first_request
def load_global_data():
    global id_list
    global job_tfidf

    query = Job.query.with_entities(Job.id, Job.job_description).order_by(Job.id.asc()).all()

    id_list = [r[0] for r in query]
    job_tfidf = Tfidf([r[1] for r in query])


@job_matches.route('/cosine_jobs')
@auth_required
def cosine_jobs():
    json_data = request.get_json()
    job = Job.query.filter_by(id=json_data['job_id']).one_or_none()

    return jsonify(get_matches(get_cosine(job_tfidf.vectorizer, job_tfidf.weights, job.job_description), job.id))


@job_matches.route('/euc_jobs')
@auth_required
def euc_jobs():
    json_data = request.get_json()
    job = Job.query.filter_by(id=json_data['job_id']).one_or_none()

    return jsonify(get_matches(get_euc(job_tfidf.vectorizer, job_tfidf.weights, job.job_description), job.id))
