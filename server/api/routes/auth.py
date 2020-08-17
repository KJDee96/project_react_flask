from flask import Blueprint, jsonify, request
from api.extensions import guard, db
from api.models.user import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    req = request
    json_data = req.get_json()

    username = json_data['username']
    password = json_data['password']

    user = guard.authenticate(username, password)
    token = guard.encode_jwt_token(user)
    return jsonify({'access_token': token, 'username': user.username, 'user_id': user.id}), 200


@auth.route('/register', methods=['POST'])
def register():
    json_data = request.get_json()
    username = json_data['username']
    password = json_data['password']

    new_user = User(username=username, password=guard.hash_password(password))
    db.session.add(new_user)
    db.session.commit()

    user = guard.authenticate(username, password)
    token = guard.encode_jwt_token(user)

    return jsonify({'access_token': token}), 200


@auth.route('/refresh')
def refresh():
    json_data = request.get_json()
    token = guard.refresh_jwt_token(json_data['token'])
    return jsonify({'access_token': token})
