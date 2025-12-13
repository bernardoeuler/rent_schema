import tkinter as tk
from database import setup 
from ui.views.register_view import RegisterView
from ui.controllers.register_controller import RegisterController

def open_register():
    controller = RegisterController()
    RegisterView(root, controller)

""" def open_login():
    for widget in root.winfo_children():
        widget.destroy()
    # aqui você criará LoginView depois
    LoginView(root, open_dashboard)
    tk.Label(root, text="Tela de login futura").pack() """

root = tk.Tk()
setup.create_tables()
open_register()
root.mainloop()
