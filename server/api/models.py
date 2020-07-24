from .extensions import db
from sqlalchemy.dialects.postgresql import ENUM

gender_enum = ENUM('male', 'female', 'other', name='enum_gender')
role_enum = ENUM('candidate', 'employer', name='enum_role')
job_type_enum = ENUM('contract_interim', 'contract_temp', 'permanent',
                     'part_time', 'temporary_seasonal', 'other',
                     'any', name='enum_job_type')

SavedJob = db.Table('saved_job',
                    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                    db.Column('job_id', db.Integer, db.ForeignKey('job.id'))
                    )

WorkExperienceSkills = db.Table('work_experience_skill',
                                db.Column('work_experience_id', db.Integer, db.ForeignKey('work_experience.id')),
                                db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'))
                                )

JobSkills = db.Table('job_skill',
                     db.Column('job_id', db.Integer, db.ForeignKey('job.id')),
                     db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'))
                     )

Application = db.Table('application',
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('job_id', db.Integer, db.ForeignKey('job.id'))
                       )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text)
    gender = db.Column(gender_enum)
    role = db.Column(role_enum)

    work_experience = db.relationship('WorkExperience', backref='users', lazy='dynamic')

    saved_jobs = db.relationship('Job', secondary=SavedJob,
                                 back_populates="saved_users")

    applications = db.relationship('Job', secondary=Application,
                                   back_populates="applicants")

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @classmethod
    def lookup(cls, userdata):
        if userdata['username'] != '':
            return cls.query.filter_by(username=userdata["username"]).one_or_none()
        else:
            return cls.query.filter_by(email=userdata["email"]).one_or_none()

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
    skills = db.relationship('Skill', secondary=JobSkills,
                             back_populates="jobs")
    applicants = db.relationship('User', secondary=Application,
                                 back_populates="applications")
    saved_users = db.relationship('User', secondary=SavedJob,
                                  back_populates="saved_jobs")

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
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    salary = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    skills = db.relationship('Skill', secondary=WorkExperienceSkills,
                             back_populates="work_experience")

    def __repr__(self):
        return '<Work Experience {}>'.format(self.position_name)


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    jobs = db.relationship('Job', secondary=JobSkills,
                           back_populates="skills")
    work_experience = db.relationship('WorkExperience', secondary=WorkExperienceSkills,
                                      back_populates="skills")
    related_skills = db.relationship('RelatedSkills', foreign_keys='RelatedSkills.skill_id',)


def __repr__(self):
    return '<Skill {}>'.format(self.name)


class RelatedSkills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
    related_skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
    skill = db.relationship('Skill', foreign_keys='RelatedSkills.related_skill_id')

    def __repr__(self):
        return '<Related Skill {}>'.format(self.id)
