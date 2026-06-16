from flask import jsonify, request
from flask import current_app as app
from src import db
from src.users import User

@app.rout('/')
def Initial_page():
    return "This page is running correctly."

