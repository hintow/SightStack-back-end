from flask import Blueprint, request, jsonify
from ..models.user import User
from ..db import db

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    required_fields = ['childName', 'childAge', 'email', 'password', 'avatar']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    # Check if email already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 400
    
    new_user = User(
        child_name=data['childName'],
        child_age=data['childAge'],
        email=data['email'],
        avatar=data['avatar']
    )
    new_user.set_password(data['password'])  # Hash the password

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
            'userId': new_user.id,
            'childName': new_user.child_name,
            'avatar': new_user.avatar
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    

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
    return jsonify({'error': 'Invalid email or password'}), 401

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


@user_bp.route('/leaderboard', methods=['GET'])
def leaderboard():
    # 获取分数最高的前 10 名用户
    top_users = User.query.order_by(User.score.desc()).limit(10).all()
    
    # 构造积分榜数据
    leaderboard_data = [
        {
            'childName': user.child_name,
            'score': user.score
        }
        for user in top_users
    ]
    
    return jsonify(leaderboard_data), 200

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_users():
    user_id = request.args.get('userId')
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'error': 'User not found'}), 404
