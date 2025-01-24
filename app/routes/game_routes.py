
from flask import Blueprint, request, jsonify
from ..models.game import Game
from ..models.word import Word
from ..models.game_word import GameWord
from ..db import db
from ..models.user import User
import random

game_bp = Blueprint('game', __name__)

# Start a new game
@game_bp.route('/games/start', methods=['POST'])
def start_game():
    data = request.get_json()
    user_id = data.get('user_id')
    level = data.get('level')

     # Check if user exists
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Create a new game record
    new_game = Game(user_id=user_id, score=0, level=level)
    db.session.add(new_game)
    db.session.commit()

    # Draw five random words from the words table
    words = Word.query.filter_by(level=level).all()
    selected_words = random.sample(words, 5)

    # Update the game_word table
    for word in selected_words:
        game_word = GameWord(game_id=new_game.id, word_id=word.id)
        db.session.add(game_word)

    db.session.commit()

    # Prepare the response
    response = {
        'game_id': new_game.id,
        'words': [{'word': word.word, 'hint': word.hint} for word in selected_words]
    }

    return jsonify(response), 201

# Get game info
@game_bp.route('/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    game = Game.query.get(game_id)
    if game:
        return jsonify(game.to_dict()), 200
    else:
        return jsonify({'error': 'Game not found'}), 404

# Get the words in the game    
@game_bp.route('/games/<int:game_id>/words', methods=['GET'])
def get_game_words(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404

    words = game.words
    return jsonify([word.to_dict() for word in words]), 200

# Update game info
@game_bp.route('/games/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'error': 'Game not found'}), 404

    data = request.get_json()
    game.score = data.get('score', game.score)
    db.session.commit()
    return jsonify(game.to_dict()), 200

