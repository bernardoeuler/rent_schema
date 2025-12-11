from database.connection import DatabaseConnection

class SampleService:
  def check_database(self):
    try:
      db = DatabaseConnection()
      conn = db.connect()
      conn.close()
      return True
    except Exception:
      return False