from models.usuario_model import Usuario
from sqlalchemy.orm import session

class usuarioRepository:
    def __init__(self,session: session):
        self.session = session

    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)

    def