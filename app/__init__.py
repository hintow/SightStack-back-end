from flask import Flask
from .db import db, migrate

def create_app():
    app = Flask(__name__)
    
    # 配置数据库URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your-database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # 初始化数据库
    db.init_app(app)
    
    # 初始化迁移
    migrate.init_app(app, db)
    
    # 注册蓝图（如果有的话）
    # from .views import main as main_blueprint
    # app.register_blueprint(main_blueprint)
    
    return app