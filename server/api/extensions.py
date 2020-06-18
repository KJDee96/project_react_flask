# https://alembic.sqlalchemy.org/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect

from flask_sqlalchemy import SQLAlchemy
from flask_praetorian import Praetorian
from flask_mail import Mail
from flask_migrate import Migrate

db = SQLAlchemy()
guard = Praetorian()
mail = Mail()
migrate = Migrate()
