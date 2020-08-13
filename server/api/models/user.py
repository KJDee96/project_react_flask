from api.extensions import db
from . import gender_enum, SavedJob, Application
from . import role_enum


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