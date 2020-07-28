from flask import Blueprint, jsonify, request
from flask_praetorian import auth_required
from api.models import Job
from api.utils import get_tfidf, get_cosine, get_doc_ids

matches = Blueprint('matches', __name__)

# initialise globals for tfidf
vector = None
weights = None


def get_tfidf_model():
    global vector
    global weights

    # set globals
    if vector is None or weights is None:
        vector, weights = get_tfidf(
                Job.query.order_by(Job.id).all()
        )
    return vector, weights


@matches.route('/matching_jobs')
@auth_required
def get_tfidf_jobs():
    json_data = request.get_json()
    job = Job.query.filter_by(id=json_data['job_id']).one_or_none().job_description
    get_tfidf_model()

    return jsonify(get_doc_ids(get_cosine(vector, weights, job)))
