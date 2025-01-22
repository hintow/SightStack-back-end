# daily challenge
# get - puzzle words from database

from flask import Blueprint, request, jsonify
import random
from ..models.word import Word
from ..db import db

word_routes = Blueprint('word_routes', __name__)

@word_routes.route('/daily_challenge', methods=['GET'])
def daily_challenge():
    num_words = 5  # The number of words selected per game
    words = Word.query.all()
    selected_words = random.sample(words, num_words)
    
    return jsonify([word.to_dict() for word in selected_words]), 200
