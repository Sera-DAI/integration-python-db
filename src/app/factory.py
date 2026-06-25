import os
from flask import Flask
from flask.json.provider import DefaultJSONProvider
from werkzeug.local import LocalProxy
from dataclasses import is_dataclass, asdict
from app.extensions import db, login_manager

class CustomJSONProvider(DefaultJSONProvider):
    def default(self, o):
        if isinstance(o, LocalProxy):
            o = o._get_current_object()
            
        if is_dataclass(o):
            return asdict(o)
        
        return super().default(o)

def create_app():
    app = Flask(__name__)
    app.json = CustomJSONProvider(app)
    
    db_user = os.getenv('MYSQL_USER')
    db_password = os.getenv('MYSQL_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('MYSQL_DATABASE')
        
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "your_secret_key"
    
    db.init_app(app)
    login_manager.init_app(app)
    
    from app.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    with app.app_context():
        from app.routes import load_routes
        load_routes(app)
        db.create_all()
        
    return app