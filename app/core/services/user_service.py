from ui.models import user_model
import hashlib

class UserService:
  @staticmethod
  def register_user(nome: str, email: str, senha: str, confirm: str):
    if not nome or not email or not senha:
      return False, "Preencha todos os campos."
    if senha != confirm:
      return False, "As senhas não coincidem."
    if user_model.get_user_by_email(email):
      return False, "Este email já está cadastrado."

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    try:
      user_model.create_user(nome, email, senha_hash)
      return True, "Usuário registrado com sucesso!"
    except Exception as e:
      return False, f"Erro ao registrar: {e}"