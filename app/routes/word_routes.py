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

    selected_word = random.sample(words, 1)[0]

    return jsonify(selected_word.to_dict()), 200

@word_routes.route('/words/level/<level>', methods=['GET'])
def get_words(level):
    # 从 session 中获取当前用户的取词索引，如果没有则初始化为 0
    if 'current_index' not in session:
        session['current_index'] = 0

    # 查询对应级别的所有单词
    words = Word.query.where(Word.level == level).all()

    if not words:
        return jsonify({"error": "No words found for the specified level"}), 404

    # 按顺序取词
    current_index = session['current_index']
    selected_word = words[current_index]

    # 更新索引，循环取词
    session['current_index'] = (current_index + 1) % len(words)

    return jsonify(selected_word.to_dict()), 200


# def get_words(level):
#     words = Word.query.where(Word.level == level).all()

#     selected_word = random.sample(words, 1)[0]
    
#     return jsonify(selected_word.to_dict()), 200
