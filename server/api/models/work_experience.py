from api.extensions import db
from . import WorkExperienceSkill


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
    skills = db.relationship('Skill', secondary=WorkExperienceSkill,
                             back_populates="work_experience")

    def __repr__(self):
        return '<Work Experience {}>'.format(self.position_name)
