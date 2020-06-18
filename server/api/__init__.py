from flask import Flask
import logging
from logging.handlers import RotatingFileHandler
import os
from .extensions import db, guard, mail, migrate
from .commands import create_test_users
from .models import User
from .routes import api
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    guard.init_app(app, User)
    mail.init_app(app)
    migrate.init_app(app, db)

    app.cli.add_command(create_test_users)

    app.register_blueprint(api)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User}

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
