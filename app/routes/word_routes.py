
from flask import Blueprint, request, jsonify
import random
from ..models.word import Word
from ..db import db
from datetime import datetime, timedelta
from sqlalchemy import func

word_routes = Blueprint('word_routes', __name__)

@word_routes.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = jsonify()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', '*')
        response.headers.add('Access-Control-Allow-Headers', '*')
        return response


# Cache per level
level_caches = {}
COOLDOWN_MINUTES = 30

def get_fresh_word(level=None):

    """
    Get a fresh word for the game while avoiding repetition
    Args:
        level: optional grade level filter
    Returns:
        tuple: (Word object or None, error message or None)
    """
        
    current_time = datetime.now()
    
    # Initialize level cache if needed
    if level not in level_caches:
        level_caches[level] = {}

    # Clean up old entries from cache
    for word_id in list(level_caches[level].keys()):
        if current_time - level_caches[level][word_id] > timedelta(minutes=COOLDOWN_MINUTES):
            del level_caches[level][word_id]
    
    # Base query
    query = Word.query
    
    if level:
        query = query.filter(Word.level == level)
    
    # Get total words for this level
    total_words = query.count()
    
    if total_words == 0:
        return None, f"No words available for level {level}"
        
    # If all words are used, reset cache
    if len(level_caches[level]) >= total_words:
        level_caches[level].clear()
        
    # Get unused word
    word = query.filter(
        ~Word.id.in_(list(level_caches[level].keys()))
    ).order_by(func.random()).first()
    
    if word:
        level_caches[level][word.id] = current_time
        return word, None
    
    return None, "Error fetching word"


@word_routes.route('/words/daily', methods=['GET'])
def daily_challenge():
    words = Word.query.all()

    selected_word = random.sample(words, 1)[0]

    return jsonify(selected_word.to_dict()), 200

@word_routes.route('/words/level/<level>', methods=['GET'])
def get_words(level):

    word, error = get_fresh_word(level)

    if error:
        return jsonify({'error': error}), 404

    return jsonify(word.to_dict()), 200
