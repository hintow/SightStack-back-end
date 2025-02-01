# daily challenge
# get - puzzle words from database

from flask import Blueprint, request, jsonify
import random
from ..models.word import Word
from ..db import db

word_routes = Blueprint('word_routes', __name__)

@word_routes.route('/words/daily', methods=['GET'])
def daily_challenge():
    words = Word.query.all()

    selected_word = random.sample(words, 1)[0]

    return jsonify(selected_word.to_dict()), 200

@word_routes.route('/words/level/<level>', methods=['GET'])
def get_words(level):
    words = Word.query.where(Word.level == level).all()

    selected_word = random.sample(words, 1)[0]
    
    return jsonify(selected_word.to_dict()), 200
