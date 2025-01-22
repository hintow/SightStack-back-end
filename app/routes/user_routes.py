# user log in 
# post - create a new user
# get - get one user

from flask import Blueprint, request, jsonify
from ..models.user import User
from ..db import db

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['POST'])  
def create_user():
    data = request.json
    user = User.from_dict(data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict())

@user_routes.route('/users/<int:user_id>', methods=['GET']) 
def get_user(user_id):
    user = User.query.get(user_id)
    return jsonify(user.to_dict())

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_routes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    data = request.json
    user.username = data['username']
    user.password_hash = data['password_hash']
    user.avatar = data['avatar']
    db.session.commit()
    return jsonify(user.to_dict())

