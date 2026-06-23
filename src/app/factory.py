import os
from flask import Flask
from app.extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    dba_dir = os.path.join(base_dir, 'instance_db')
    
    if not os.path.exists(dba_dir):
        os.makedirs(dba_dir)
        print(f"Diretório criado com sucesso em {dba_dir}")
        
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dba_dir, 'database.db')
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