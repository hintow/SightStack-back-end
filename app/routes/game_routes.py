
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
    if request.method == 'OPTIONS':
        # 返回允许的 CORS 头部
        response = jsonify()
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
          
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