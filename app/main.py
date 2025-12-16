import tkinter as tk
from views.register_view import RegisterView
from controllers.register_controller import RegisterController

def main():
    root = tk.Tk()
    controller = RegisterController()
    RegisterView(root, controller)
    root.mainloop()

if __name__ == "__main__":
    main()
