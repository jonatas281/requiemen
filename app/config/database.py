from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Definindo parametros para acesso ao banco de dados 
db_use = "aluno"
db_password = "aluno_senha"
db_name = "meu_banco_senai"
db_host = "localhost"
db_port = "3306"

#endereço  (URL) para conexao com banco de dados.
DATABASE_URL = f"mysql+pymysql://{db_password}@{db_port}/{db_name}"

# criando banco de dados
db = create_engine(DATABASE_URL)
# criando conexão com banco de dados
Session = sessionmaker(bind=db)
session = Session()

#gerenciamento conexao com banco de dados.
@contextmanager
def get_db():
    db = session()
    try:
        yield db # realiza tentativa de operação do bd
        db.commit()#salvar no db.
    except Exception as erro:
        db.rollback()#caso ocorra algum erro, desfaz alteraçãoes no db
        raise erro # caso ocorra algum erro,mostra mensagem erro no terminal
    finally:
            db.close()  # fecha conexão com db