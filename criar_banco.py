from rede import database, app
from rede.models import User, Photo

with app.app_context():
    database.create_all()

