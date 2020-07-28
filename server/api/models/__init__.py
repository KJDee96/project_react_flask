from sqlalchemy.dialects.postgresql import ENUM
from api.extensions import db

gender_enum = ENUM('male', 'female', 'other', name='enum_gender')
role_enum = ENUM('candidate', 'employer', name='enum_role')
job_type_enum = ENUM('contract_interim', 'contract_temp', 'permanent',
                     'part_time', 'temporary_seasonal', 'other',
                     'any', name='enum_job_type')

SavedJob = db.Table('saved_job',
                    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                    db.Column('job_id', db.Integer, db.ForeignKey('job.id'))
                    )

WorkExperienceSkill = db.Table('work_experience_skill',
                                db.Column('work_experience_id', db.Integer, db.ForeignKey('work_experience.id')),
                                db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'))
                                )

JobSkill = db.Table('job_skill',
                     db.Column('job_id', db.Integer, db.ForeignKey('job.id')),
                     db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'))
                     )

Application = db.Table('application',
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('job_id', db.Integer, db.ForeignKey('job.id'))
                       )
