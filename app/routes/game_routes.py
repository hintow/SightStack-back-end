# define game-related routes. These routes can handle operations such as 
# creating a game, getting game information, updating a game

from flask import Blueprint, request, jsonify
from ..models.game import Game
from ..models.word import Word
from ..db import db

game_bp = Blueprint('game', __name__)

# Create a game
@game_bp.route('/games', methods=['POST'])
def create_game():
    data = request.get_json()
    new_game = Game.from_dict(data)
    db.session.add(new_game)
    db.session.commit()
    return jsonify(new_game.to_dict()), 201

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
    game.level = data.get('level', game.level)
    db.session.commit()
    return jsonify(game.to_dict()), 200