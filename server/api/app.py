from flask import Flask
from api.routes.auth import auth
from api.routes.matches import matches
from .extensions import db, guard, migrate
from .commands import import_data, generate_apps, generate_skills
from config.config import Config
from .models.user import User
from .models.job import Job
from .models.work_experience import WorkExperience
from .models.skill import Skill
from .models.related_skill import RelatedSkill
from .models import Application, SavedJob, JobSkill, WorkExperienceSkill


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # extensions
    db.init_app(app)
    guard.init_app(app, User)
    migrate.init_app(app, db)

    # extra commands
    app.cli.add_command(import_data)
    app.cli.add_command(generate_apps)
    app.cli.add_command(generate_skills)

    # blueprints
    app.register_blueprint(auth)
    app.register_blueprint(matches)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User, 'Job': Job, 'Application': Application, 'SavedJob': SavedJob,
                'WorkExperience': WorkExperience, 'Skill': Skill, 'RelatedSkill': RelatedSkill,
                'WorkExperienceSkill': WorkExperienceSkill, 'JobSkill': JobSkill}

    return app
