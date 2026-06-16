import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    dba_dir = os.path.join(base_dir, 'dba')
    
    if not os.path.exists(dba_dir):
        os.makedirs(dba_dir)
        
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dba_dir, 'database.db')
    app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "your_secret_key"
    
    db.init_app(app)
    
    with app.app_context():
        from src import users
        db.create_all()
        
    return app 