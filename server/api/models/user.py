from api.extensions import db
from . import gender_enum, Application
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
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    country = db.Column(db.Text)
    zipcode = db.Column(db.Text)
    degree_type = db.Column(db.Text)
    major = db.Column(db.Text)
    graduation_date = db.Column(db.Date)
    work_history_count = db.Column(db.Integer)
    work_history_years_experience = db.Column(db.Integer)
    employed = db.Column(db.Boolean)
    managed_others = db.Column(db.Boolean)
    managed_how_many = db.Column(db.Integer)

    applications = db.relationship('Job', secondary=Application,
                                   back_populates="applicants")

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

    # https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
