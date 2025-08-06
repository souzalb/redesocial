from rede import database, app
from rede.models import Users, Photo

with app.app_context():
    database.create_all()

