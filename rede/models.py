from rede import database
from datetime import datetime, timezone

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(20), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(60), nullable=False)
    photos = database.relationship('Photo', backref='user', lazy=True)

class Photo(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    file_name = database.Column(database.String(255), default="default.png")
    upload_date = database.Column(database.DateTime, nullable=False, default=datetime.now(timezone.utc))
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)

