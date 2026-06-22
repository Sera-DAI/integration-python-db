from app.extensions import db
from dataclasses import dataclass

class User(db.Model):
    id: int
    username: str
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)