import os
from flask import Flask
from .db import db, migrate
from dotenv import load_dotenv
# from .models.user import user_bp  
# from .routes.word_routes import word_routes

load_dotenv() 

def create_app():
    app = Flask(__name__)
    
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/sightstack_dev'
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    migrate.init_app(app, db)
    
    # app.register_blueprint(user_bp, url_prefix='/api')
    # app.register_blueprint(word_routes, url_prefix='/api')  
    
    return app