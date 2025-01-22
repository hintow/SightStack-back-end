from flask import Flask
from .db import db, migrate
from .models.user import user_bp  

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/sightstack_dev'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    migrate.init_app(app, db)
    
    app.register_blueprint(user_bp, url_prefix='/api')
    
    return app