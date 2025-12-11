import mariadb
from config.settings import DB_CONFIG

class DatabaseConnection:
  def connect(self):
    return mariadb.connect(
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        host=DB_CONFIG['host'],
        port=DB_CONFIG['port'],
        database=DB_CONFIG['database']
    )