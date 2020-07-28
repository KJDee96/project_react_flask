from api.extensions import db


class RelatedSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
    related_skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
    skill = db.relationship('Skill', foreign_keys='RelatedSkill.related_skill_id')

    def __repr__(self):
        return '<Related Skill {}>'.format(self.id)
