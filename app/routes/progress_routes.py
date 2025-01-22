#save progress - post
# 

from flask import Blueprint, jsonify, request
from ..models.word import Word
import random
from ..models.progress import UserProgress
from .. import db

progress_bp = Blueprint('progress', __name__)
    
@progress_bp.route('/save_progress', methods=['POST'])
def save_progress():
    data = request.get_json()
    progress = UserProgress.from_dict(data)
    
    db.session.add(progress)
    db.session.commit()
    
    return jsonify(progress.to_dict()), 201

@progress_bp.route('/progress/<int:user_id>', methods=['GET'])
def get_progress(user_id):
    progress = UserProgress.query.filter_by(user_id=user_id).all()
    return jsonify([p.to_dict() for p in progress]), 200