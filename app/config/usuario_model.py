from sqlalchemy import Column , String, Integer
from sqlalchemy.orm import declarative_base
from config.database import db

# base para criar tabelas no banco de dados
base = declarative_base()

class Usuario(base):
    # definindo caracteristicas no banco de dados 
    __tablename__ = "usuario"

    id = Column(String(150))
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    # definindo caracteristicas da classe 
    def __int__(self,nome:str,email: str ,senha:str):
        self.nome = nome 
        self.email = email
        self.senha = senha
# criando tabela no banco de dados.
base.metadata.create_all(bind=db)