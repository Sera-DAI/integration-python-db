from flask import jsonify, request
from flask_login import login_user, logout_user, login_required, current_user
from app.extensions import db
from app.models import User

def load_routes(app):

    @app.route('/') 
    def Initial_page():
        return "This page being running correctly"
    
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        
        if not data.get('username') or not data.get('password'):
            return jsonify({"Message": "Username and password is necessary for authentication"}), 400
        
        if User.query.filter_by(username=data.get('username')).first():
            return jsonify({"Error": "User already registered"}), 400
        
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
            return jsonify({"Message": "Login successful", "user": user.username})
        
        return jsonify({"Error": "Invalid  credentials"}), 401
    
    @app.route('/return_users', methods=['GET'])
    @login_required
    def return_users():
        users = User.query.all()
        return jsonify({"Message": "List of all users registered"}, users), 200
        
    @app.route('/return_user_id/<int:user_id>', methods=['GET'])
    @login_required
    def return_user_id(user_id):
        return jsonify({
            "Message": "Requested user",
            "User": User.query.filter_by(id=user_id).first()
        })
        
    @app.route('/dashboard', methods=['GET'])
    @login_required
    def dashboard():
        return jsonify(current_user)
    
    @app.route('/logout', methods=['POST'])
    @login_required
    def logout():
        logout_user()
        return jsonify({
            "Message": "Logout successfuly"
        })