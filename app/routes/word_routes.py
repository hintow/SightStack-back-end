# daily challenge
# get - puzzle words from database

from flask import Blueprint, request, jsonify
import random
from ..models.word import Word
from ..db import db

word_routes = Blueprint('word_routes', __name__)

NUM_WORDS_DAILY_CHALLENGE = 10
NUM_WORDS_GET_WORDS = 5

@word_routes.route('/daily_challenge', methods=['GET'])
def daily_challenge():
    words = Word.query.all()

    selected_words = random.sample(words, NUM_WORDS_DAILY_CHALLENGE)
    return jsonify([word.to_dict() for word in selected_words]), 200

@word_routes.route('/get_words', methods=['GET'])
def get_words():
    words = Word.query.all()   

    selected_words = random.sample(words, NUM_WORDS_GET_WORDS)
    return jsonify([word.to_dict() for word in selected_words]), 200
