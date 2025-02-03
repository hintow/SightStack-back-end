
from flask import Blueprint, request, jsonify
import random
from ..models.word import Word
from ..db import db
from datetime import datetime, timedelta
from sqlalchemy import func

word_routes = Blueprint('word_routes', __name__)

# Cache to store recently served words
recently_used_words = {}
COOLDOWN_MINUTES = 30

def get_fresh_word(level=None):
    current_time = datetime.now()
    # Clean up old entries from cache
    for word_id in list(recently_used_words.keys()):
        if current_time - recently_used_words[word_id] > timedelta(minutes=COOLDOWN_MINUTES):
            del recently_used_words[word_id]
            
    # Base query
    query = Word.query
    
    if level:
        query = query.filter(Word.level == level)
    
    # Exclude recently used words
    if recently_used_words:
        query = query.filter(~Word.id.in_(list(recently_used_words.keys())))
    
    # Get word ordered by ID to ensure consistent progression
    word = query.order_by(func.random()).first()
    
    # If no unused words available, reset cache and try again
    if not word and recently_used_words:
        recently_used_words.clear()
        word = query.order_by(func.random()).first()
    
    if word:
        recently_used_words[word.id] = current_time
        
    return word


@word_routes.route('/words/daily', methods=['GET'])
def daily_challenge():
    words = Word.query.all()

    selected_word = random.sample(words, 1)[0]

    return jsonify(selected_word.to_dict()), 200

@word_routes.route('/words/level/<level>', methods=['GET'])
def get_words(level):
    word = get_fresh_word(level)
    if not word:
        return jsonify({'error': f'No words available for level {level}'}), 404
    return jsonify(word.to_dict()), 200
