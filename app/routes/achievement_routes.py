from flask import Blueprint, request, jsonify
from ..models.user_achievements import UserAchievements
from ..db import db

achievement_bp = Blueprint('user_achievements', __name__)

@achievement_bp.route('/achievements', methods=['POST'])
def create_achievement():
    data = request.get_json()
    new_achievement = UserAchievements.from_dict(data)
    db.session.add(new_achievement)
    db.session.commit()
    return jsonify(new_achievement.to_dict()), 201

@achievement_bp.route('/achievements/user/<int:user_id>', methods=['GET'])
def get_user_achievements(user_id):
    achievements = UserAchievements.query.filter_by(user_id=user_id).all()
    return jsonify([achievement.to_dict() for achievement in achievements]), 200