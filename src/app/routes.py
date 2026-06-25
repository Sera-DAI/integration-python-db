from flask import jsonify, request
from flask_login import login_user, logout_user, login_required, current_user
from app.extensions import db
from app.models import User

def load_routes(app):

    @app.route('/') 
    def Initial_page():
        return "This page being running correctly."
    
    @app.route('/api/register', methods=['POST'])
    def register():
        data = request.get_json()
        
        if not data.get('username') or not data.get('password'):
            return jsonify({
                "Message": "Username and password is necessary for authentication."}), 400
        
        if User.query.filter_by(username=data.get('username')).first():
            return jsonify({
                "Error": "User already registered."}), 400
        
        new_user = User(username=data.get('username'))
        new_user.set_password(data.get('password'))
        
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user), 201
    
    @app.route('/api/login', methods=['POST'])
    def login():
        data = request.get_json()
        user = User.query.filter_by(username=data.get('username')).first()
        
        if user and user.check_password(data.get('password')):
            login_user(user)
            return jsonify({
                "Message": "Login successful.", "user": user.username
            })
        
        return jsonify({"Error": "Invalid  credentials."}), 401
    
    @app.route('/user/return_users', methods=['GET'])
    @login_required
    def return_users():
        users = User.query.all()
        return jsonify({"Message": "List of all users registered."}, users), 200
        
    @app.route('/user/return_user_id/<int:user_id>', methods=['GET'])
    @login_required
    def return_user_id(user_id):
        user = User.query.filter_by(id=user_id).first()
        if user == None:
            return jsonify({
                "Message": "User not found by ID."
            }), 404
        return jsonify({
            "Message": "Requested user.",
            "User": user
        })
        
    @app.route('/user/dashboard', methods=['GET'])
    @login_required
    def dashboard():
        return jsonify(current_user)
    
    @app.route('/user/update_password', methods=['PUT'])
    @login_required
    def update_password():
        data = request.get_json()
        user = User.query.filter_by(username=data.get('username')).first()
        
        if data.get('username') != current_user.username:
            return jsonify({
                "Message": "Provided username doesn't match the current user"
            }), 401
        elif not data.get('password') or not data.get('new_password'):
            return jsonify({
                "Message": "Current and new password is required."
            }), 400        
        elif not user.check_password(data.get('password')):
            return jsonify({
                "Message": "Invalid current password."
            }), 400
        
        user.set_password(data.get('new_password'))
        db.session.commit()        
        logout_user()
        
        return jsonify({
            "Message": "Password updated successfuly. You have been logged out and must log in again."
        })
        
    @app.route('/user/delete_user', methods=['DELETE'])
    @login_required
    def delete_user():
        data = request.get_json()
        user = User.query.filter_by(id=data.get('id')).first()
        
        if data.get('username') != current_user.username and data.get('username') is not "":
            return jsonify({
                "Message": "Provided username doesn't match the current user.",
            }), 401
        elif not data.get('password') or not data.get('username') and data.get('username') is "" or not data.get('id') :
            return jsonify({
                "Message": "Current id, password and username is required."
            }), 400
        elif not user.check_password(data.get('password')) or data.get('id') != current_user.id:
            return jsonify({
                "Message": "Invalid password or id."
            }), 400
        
        db.session.delete(user)
        db.session.commit()
        return jsonify({
            "Message": "Your user has been deleted."
        })
    @app.route('/user/logout', methods=['POST'])
    @login_required
    def logout():
        logout_user()
        return jsonify({
            "Message": "Logout successfuly."
        })