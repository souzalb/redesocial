from rede import database, app
from rede.models import Users, Photo
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
import time

def wait_for_db(max_retries=5, delay=5):
    retries = 0
    while retries < max_retries:
        try:
            with app.app_context():
                # Tenta estabelecer conexão
                database.engine.connect()
                print("Conexão com o banco de dados estabelecida com sucesso!")
                return True
        except OperationalError as e:
            retries += 1
            print(f"Tentativa {retries} de {max_retries} falhou. Aguardando {delay} segundos...")
            time.sleep(delay)
    return False

if wait_for_db():
    with app.app_context():
        try:
            database.create_all()
            print("Tabelas criadas com sucesso!")
        except Exception as e:
            print(f"Erro ao criar tabelas: {str(e)}")
else:
    print("Não foi possível estabelecer conexão com o banco de dados após várias tentativas.")