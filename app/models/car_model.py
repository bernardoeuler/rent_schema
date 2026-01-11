# src/models/car_model.py
from ..database.connection import DatabaseConnection

class CarModel:
  def __init__(self):
    pass
  
  def create_car(self, placa: str, chassi: str, cor: str, ano: int, quilometragem: int, status: str, ano_fabricacao: int, id_modelo: int):
    conn = DatabaseConnection.get_connection()
    cursor = conn.cursor()
    cursor.execute("""
      INSERT INTO Carro (Placa, Chassi, Cor, Ano, Quilometragem, Status, ano_fabricacao, fk_Modelo_ID_Modelo)
      VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (placa, chassi, cor, ano, quilometragem, status, ano_fabricacao, id_modelo))

    conn.commit()
    cursor.close()
    conn.close()