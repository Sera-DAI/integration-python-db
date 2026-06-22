from flask import jsonify
from app.database import db
from app.models import User

def load_routes(app):
    

    @app.route('/') 
    def Initial_page():
        return "This page is running correctly."   