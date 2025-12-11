from database.connection import DatabaseConnection

def get_users():
  db = DatabaseConnection()
  conn = db.connect()
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM usuarios")
  result = cursor.fetchall()
  cursor.close()
  conn.close()
  return result