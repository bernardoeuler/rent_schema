import tkinter as tk
from tkinter import ttk
from ui.controllers.main_controller import MainController
from ui.styles.theme import apply_theme

class MainWindow(tk.TK):
  def __init__(self):
    super().__init__()
  
    self.title('Aluguel de Carros')
    self.geometry('900x600')
    
    apply_theme(self)

    self.controller = MainController()

    ttk.Label(self, texxt="Tela Principal", font=("Arial", 18)).pack(pady=20)

    ttk.Button(self, text="Testar Conexão com BD", command=self.test_db).pack(pady=10)

  def test_db(self):
    ok = self.controller.test_connection()
    msg = "Conexão bem sucedida!" if ok else "Falha na conexão."
    tk.messagebox.showinfo("Resultado", msg)