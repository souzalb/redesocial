from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://banco_redesocial_user:3SfcoCPEGbZENoxhk3t4ac19QDLfShhz@dpg-d28l2muuk2gs73ffhdo0-a.oregon-postgres.render.com/banco_redesocial"
app.config['SECRET_KEY'] = '3SfcoCPEGbZENoxhk3t4ac19QDLfShhz'
app.config['UPLOAD_FOLDER'] = 'static/posts_photos'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'

from rede import routes



