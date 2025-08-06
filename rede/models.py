from rede import database, login_manager
from datetime import datetime
from flask_login import UserMixin
from zoneinfo import ZoneInfo

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(20), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(60), nullable=False)
    photos = database.relationship('Photo', backref='user', lazy=True)

class Photo(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    file_name = database.Column(database.String(255), default="default.png")
    upload_date = database.Column(database.DateTime, nullable=False, default=lambda: datetime.now(ZoneInfo("America/Sao_Paulo")))
    user_id = database.Column(database.Integer, database.ForeignKey('Users.id'), nullable=False)

