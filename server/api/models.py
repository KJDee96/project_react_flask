from .extensions import db
from sqlalchemy.dialects.postgresql import ENUM

gender_enum = ENUM('male', 'female', 'other', name='enum_gender')
role_enum = ENUM('candidate', 'employer', name='enum_role')
job_type_enum = ENUM('contract_interim', 'contract_temp', 'permanent',
                     'part_time', 'temporary_seasonal', 'other',
                     'any', name='enum_job_type')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text)
    gender = db.Column(gender_enum)
    role = db.Column(role_enum)
    work_experience = db.relationship('work_experience', backref='user', lazy='dynamic')
    saved_jobs = db.relationship('saved_jobs', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.filter_by(id=id).one_or_none()

    @property
    def rolenames(self):
        return []

    @property
    def identity(self):
        return self.id


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

    def __repr__(self):
        return '<Job {}>'.format(self.job_title)


class WorkExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    employer_name = db.Column(db.Text)
    position_name = db.Column(db.Text)
    job_description = db.Column(db.Text)
    city = db.Column(db.Text)
    county = db.Column(db.Text)
    postcode = db.Column(db.Text)
    end_date = db.Column(db.Date)
    salary = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return '<Work Experience {}>'.format(self.position_name)


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __repr__(self):
        return '<Skill {}>'.format(self.name)


class SavedJob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))

    def __repr__(self):
        return '<Saved Job {}>'.format(self.id)
