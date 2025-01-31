# daily challenge
# get - puzzle words from database

from flask import Blueprint, request, jsonify, session
import random
from ..models.word import Word
from ..db import db

word_routes = Blueprint('word_routes', __name__)

@word_routes.route('/words/daily', methods=['GET'])
def daily_challenge():
    words = Word.query.all()
    used_words = session.get("used_words", set())

    available_words = [word for word in words if word.id not in used_words]

    if not available_words:
        session["used_words"] = set()
        available_words = words

    selected_word = random.sample(words, 1)[0]
    used_words.add(selected_word.id)
    session["used_words"] = used_words  # 更新 session

    return jsonify(selected_word.to_dict()), 200

@word_routes.route('/words/level/<level>', methods=['GET'])
def get_words(level):
    words = Word.query.where(Word.level == level).all()
    used_words = session.get(f"used_words_level_{level}", set())

    available_words = [word for word in words if word.id not in used_words]
    
    if not available_words:
        session[f"used_words_level_{level}"] = set()
        available_words = words

    selected_word = random.sample(words, 1)[0]
    used_words.add(selected_word.id)
    session[f"used_words_level_{level}"] = used_words  # 更新 session
    
    return jsonify(selected_word.to_dict()), 200
