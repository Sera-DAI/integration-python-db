from flask import jsonify, request
from flask_login import login_user, logout_user, login_required, current_user
from app.extensions import db
from app.models import User

def load_routes(app):

    @app.route('/') 
    def Initial_page():
        return 'This page being running corretly'
    
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        if data.get('username') or data.get('password'):
            return jsonify({'Message': 'Username and password is necessary for authentication'}), 400
        
        if User.query.filter_by(username=data.get('username')).first():
            return jsonify({'Error': 'User already registered'}), 400
        
        new_user = User(username=data.get('username'))
        new_user.set_password(data.get('password'))
        
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user), 201
    
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        user = User.query.filter_by(username=data.get('username')).first()
        
        if user and user.check_password(data.get('password')):
            login_user(user)
            return jsonify({'message': 'Login completed with success', 'user': user})
        
        return jsonify({'error': 'Invalid  credentials'}), 401
    
    @app.route('/return_users', methods=['GET'])
    @login_required
    def return_users():
        users = User.query.all()
        return jsonify(users), 200
        