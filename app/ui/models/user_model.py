# src/models/user_model.py
from database.connection import DatabaseConnection

def create_user(nome: str, email: str, senha_hash: str):
  conn = DatabaseConnection.get_connection()
  cursor = conn.cursor()

  cursor.execute("""
    INSERT INTO usuarios (nome, email, senha)
    VALUES (?, ?, ?)
  """, (nome, email, senha_hash))

  conn.commit()
  cursor.close()
  conn.close()

def get_user_by_email(email: str) -> bool:
  conn = DatabaseConnection.get_connection()
  cursor = conn.cursor()

  cursor.execute("SELECT id FROM usuarios WHERE email = ?", (email,))
  result = cursor.fetchone()

  cursor.close()
  conn.close()
  return result is not None
