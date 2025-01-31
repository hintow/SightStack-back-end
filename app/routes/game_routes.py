
from flask import Blueprint, request, jsonify
from ..models.game import Game
from ..models.word import Word
from ..models.game_word import GameWord
from ..db import db
from ..models.user import User
import random
from ..models.achievement import Achievement

game_bp = Blueprint('game', __name__)

@game_bp.route('/update', methods=['POST'])
def update_score():
    data = request.get_json()
    user = User.query.get(data['userId'])
    user.score += data['score']
    achievements_unlocked = []
    for achievement in Achievement.query.all():
        if user.score >= achievement.required_score and achievement not in user.achievements:
            user.achievements.append(achievement)
            achievements_unlocked.append(achievement.title)
    db.session.commit()
    return jsonify({
        'newScore': user.score,
        'achievementsUnlocked': achievements_unlocked
    }), 200