from core.services.user_service import UserService
from views.login_view import LoginView

class RegisterController:
  def set_view(self, view):
    self.view = view
  
  def register(self):
    nome = self.view.get_nome()
    email = self.view.get_email()
    senha = self.view.get_senha()
    confirm = self.view.get_confirm()
    
    result, msg = UserService.register_user(nome, email, senha, confirm)
    
    if result:
      self.view.show_info("Sucesso!", msg)
      self.view.go_to_login()
    else:
      self.view.show_error("Erro!", msg)

  def go_to_login(self):
    self.view.show_frame("LoginView")
    
    login_controller = LoginController()
    LoginView(root, login_controller)