from api.extensions import db
from . import JobSkill, WorkExperienceSkill


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    jobs = db.relationship('Job', secondary=JobSkill,
                           back_populates="skills")
    work_experience = db.relationship('WorkExperience', secondary=WorkExperienceSkill,
                                      back_populates="skills")
    related_skills = db.relationship('RelatedSkill', foreign_keys='RelatedSkill.skill_id', )

    def __repr__(self):
        return '<Skill {}>'.format(self.name)
