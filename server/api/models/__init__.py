from sqlalchemy.dialects.postgresql import ENUM
from api.extensions import db

gender_enum = ENUM('male', 'female', 'other', name='enum_gender')
role_enum = ENUM('candidate', 'employer', name='enum_role')

Application = db.Table('application',
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('job_id', db.Integer, db.ForeignKey('job.id'))
                       )
