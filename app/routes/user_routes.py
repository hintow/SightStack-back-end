# user log in 
# post - create a new user
# get - get one user/ get all users

from flask import Blueprint, request, jsonify
from ..models.user import User
from ..db import db

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check if email already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 400

    new_user = User(
        child_name=data['childName'],
        child_age=data['childAge'],
        email=data['email'],
        # password_hash=data['password'],  # 在生产环境中，记得对密码进行哈希处理！
        avatar=data['avatar']
    )
    new_user.set_password(data['password']) # hash password

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'userId': new_user.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        return jsonify({
            'userId': user.id,
            'childName': user.child_name,
            'avatar': user.avatar,
            'score': user.score,
            'achievements': [a.title for a in user.achievements]
        }), 200
    return jsonify({'error': 'Invalid credentials'}), 401

@user_bp.route('/userInfo', methods=['GET'])
def user_info():
    user_id = request.args.get('userId')
    user = User.query.get(user_id)
    if user:
        return jsonify({
            'childName': user.child_name,
            'childAge': user.child_age,
            'avatar': user.avatar,
            'score': user.score,
            'achievements': [a.title for a in user.achievements]
        }), 200
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404


