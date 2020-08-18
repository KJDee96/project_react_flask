import math
from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required
from sqlalchemy.orm.exc import NoResultFound
from api.models.job import Job
from api.utils import get_cosine, get_euc, get_doc_ids, Tfidf

jobs = Blueprint('jobs', __name__)

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


@jobs.before_app_first_request
def load_global_data():
    global id_list
    global job_tfidf

    query = Job.query.with_entities(Job.id, Job.job_description).order_by(Job.id.asc()).all()

    id_list = [r[0] for r in query]
    job_tfidf = Tfidf([r[1] for r in query])


@jobs.route('/jobs/all', methods=['GET'])
@auth_required
def jobs_all():
    query = Job.query.order_by(Job.end_date.desc())
    if 'page' in request.args:
        page = int(request.args['page'])
        return jsonify({'total': math.ceil(query.paginate(page, 10, False).total / 10), 'jobs': [job.as_dict() for job in query.paginate(page, 10, False).items]})
    else:
        return jsonify({'total': math.ceil(query.paginate(1, 10, False).total / 10), 'jobs': [job.as_dict() for job in query.paginate(1, 10, False).items]})


@jobs.route('/jobs/<job_id>', methods=['GET'])
@auth_required
def get_job(job_id):
    if job_id:
        try:
            return jsonify(Job.query.filter_by(id=job_id).one().as_dict())
        except NoResultFound:
            return "No result found"
    else:
        return "Error: No id field provided. Please specify an id."


@jobs.route('/jobs/matching/<sim_type>/<job_id>', methods=['GET'])
@auth_required
def matching_jobs(sim_type, job_id):
    job = Job.query.filter_by(id=job_id).one_or_none()
    if sim_type == 'cosine':
        return jsonify(get_matches(get_cosine(job_tfidf.vectorizer, job_tfidf.weights, job.job_description), job.id))
    elif sim_type == 'euclidean':
        return jsonify(get_matches(get_euc(job_tfidf.vectorizer, job_tfidf.weights, job.job_description), job.id))
