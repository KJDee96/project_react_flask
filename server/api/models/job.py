from api.extensions import db
from . import job_type_enum, JobSkill, Application, SavedJob


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Text)
    company_name = db.Column(db.Text)
    job_description = db.Column(db.Text)
    job_title = db.Column(db.Text)
    job_type = db.Column(job_type_enum)
    location = db.Column(db.Text)
    post_date = db.Column(db.Date)
    salary_offered = db.Column(db.Text)
    skills = db.relationship('Skill', secondary=JobSkill,
                             back_populates="jobs")
    applicants = db.relationship('User', secondary=Application,
                                 back_populates="applications")
    saved_users = db.relationship('User', secondary=SavedJob,
                                  back_populates="saved_jobs")

    def __repr__(self):
        return '<Job {}>'.format(self.job_title)
