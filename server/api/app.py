from flask import Flask
from api.routes.auth import auth
from api.routes.matches import matches
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

    app.register_blueprint(auth)
    app.register_blueprint(matches)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User, 'Job': Job, 'Application': Application, 'SavedJob': SavedJob,
                'WorkExperience': WorkExperience, 'Skill': Skill, 'RelatedSkills': RelatedSkills,
                'WorkExperienceSkills': WorkExperienceSkills, 'JobSkills': JobSkills}

    return app
