import os
import logging
from flask import Flask

from logging.handlers import RotatingFileHandler

from .routes import api
from .extensions import db, guard, migrate
from .commands import import_data, generate_apps, generate_skills
from .models import User, Job, WorkExperience, Skill, RelatedSkills, SavedJob, \
    WorkExperienceSkills, JobSkills, Application

from config.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    guard.init_app(app, User)
    migrate.init_app(app, db)

    app.cli.add_command(import_data)
    app.cli.add_command(generate_apps)
    app.cli.add_command(generate_skills)
    app.register_blueprint(api)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User, 'Job': Job, 'Application': Application, 'SavedJob': SavedJob,
                'WorkExperience': WorkExperience, 'Skill': Skill, 'RelatedSkills': RelatedSkills,
                'WorkExperienceSkills': WorkExperienceSkills, 'JobSkills': JobSkills}

    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/flask.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    return app
