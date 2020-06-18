import click
from flask.cli import with_appcontext
from .extensions import guard, db
from .models import User


@click.command(name='create_test_users')
@with_appcontext
def create_test_users():
    user1 = User(username='User1', password=guard.hash_password('test'))
    user2 = User(username='User2', password=guard.hash_password('test'))
    user3 = User(username='User3', password=guard.hash_password('test'))

    db.session.add_all([user1, user2, user3])
    db.session.commit()
