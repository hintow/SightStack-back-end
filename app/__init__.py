import os
from flask import Flask
from .db import db, migrate
from dotenv import load_dotenv
from .models.user import User
from .models.game import Game
from .models.word import Word
from .models.user_achievement import UserAchievement
from .models.game_word import GameWord
from .models.achievement import Achievement
from .routes.game_routes import game_bp
from .routes.user_routes import user_bp

load_dotenv() 

def create_app(config=None):
    app = Flask(__name__)
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/sightstack_dev'
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    if config:
        app.config.update(config)

    db.init_app(app)    
    migrate.init_app(app, db)

    app.register_blueprint(game_bp)
    app.register_blueprint(user_bp)
    
    # app.register_blueprint(user_bp, url_prefix='/api')
    # app.register_blueprint(word_routes, url_prefix='/api')  
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)