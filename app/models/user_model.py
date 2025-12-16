# src/models/user_model.py
from database.connection import DatabaseConnection

class UserModel:
  def __init__(self):
    pass
  
  def create_user(self, nome: str, email: str, senha_hash: str):
    conn = DatabaseConnection.get_connection()
    cursor = conn.cursor()
    cursor.execute("""
      INSERT INTO clientes (nome, email, senha)
      VALUES (?, ?, ?)
    """, (nome, email, senha_hash))

    conn.commit()
    cursor.close()
    conn.close()

  def get_user_by_email(self, email: str) -> bool:
    conn = DatabaseConnection.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM clientes WHERE email = ?", (email,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()
    return result is not None
