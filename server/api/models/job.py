from api.extensions import db
from . import Application


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.Text)
    job_description = db.Column(db.Text)
    requirements = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    country = db.Column(db.Text)
    zipcode = db.Column(db.Text)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    applicants = db.relationship('User', secondary=Application,
                                 back_populates="applications")

    def __repr__(self):
        return '<Job {}>'.format(self.job_title)

    # https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
