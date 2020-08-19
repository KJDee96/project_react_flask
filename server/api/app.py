from flask import Flask
from api.routes.auth import auth
from api.routes.jobs import jobs
from api.routes.users import users
from .extensions import db, guard, migrate
from .commands import import_users, import_jobs, import_apps
from config.config import Config
from .models.user import User
from .models.job import Job
from .models import Application


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # extensions
    db.init_app(app)
    guard.init_app(app, User)
    migrate.init_app(app, db)

    # extra commands
    app.cli.add_command(import_users)
    app.cli.add_command(import_jobs)
    app.cli.add_command(import_apps)

    # blueprints
    app.register_blueprint(auth)
    app.register_blueprint(jobs)
    app.register_blueprint(users)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User, 'Job': Job, 'Application': Application}

    return app
