# user log in 
# post - create a new user
# get - get one user/ get all users

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
    return jsonify(user.to_dict()), 201

@user_routes.route('/users/<int:user_id>', methods=['GET']) 
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200


