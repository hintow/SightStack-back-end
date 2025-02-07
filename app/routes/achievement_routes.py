from flask import Blueprint, request, jsonify
from ..models.user import User
from ..models.achievement import Achievement
from ..models.user_achievement import UserAchievement
from ..db import db

achievement_bp = Blueprint('user_achievements', __name__)

@achievement_bp.route('/achievements/check/<int:user_id>', methods=['POST'])
def check_achievements(user_id):
    """Check and unlock achievements based on user's score"""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Get all achievements user hasn't unlocked yet
    available_achievements = Achievement.query.filter(
        ~Achievement.id.in_(
            db.session.query(UserAchievement.achievement_id)
            .filter(UserAchievement.user_id == user_id)
        )
    ).all()

    newly_unlocked = []
    for achievement in available_achievements:
        if user.score >= achievement.required_score:
            # Create new user achievement
            user_achievement = UserAchievement(
                user_id=user_id,
                achievement_id=achievement.id
            )
            db.session.add(user_achievement)
            newly_unlocked.append(achievement.to_dict())

    try:
        db.session.commit()
        return jsonify({
            'message': 'Achievements updated',
            'newly_unlocked': newly_unlocked
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@achievement_bp.route('/achievements/user/<int:user_id>', methods=['GET'])
def get_user_achievements(user_id):
    """Get all achievements for a user with unlock status"""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Get all achievements
    all_achievements = Achievement.query.all()
    
    # Get user's unlocked achievements
    unlocked_ids = set(ua.achievement_id for ua in user.user_achievements)
    
    achievements_data = [{
        **achievement.to_dict(),
        'unlocked': achievement.id in unlocked_ids
    } for achievement in all_achievements]

    return jsonify(achievements_data), 200