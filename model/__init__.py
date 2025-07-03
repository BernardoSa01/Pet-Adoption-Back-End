from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Criação do diretório database, caso não exista
db_path = "database/"
if not os.path.exists(db_path):
  os.makedirs(db_path)

# URL de conexão com o banco SQLite
DATABASE_URL = "sqlite:///./database/pet_adoption.db"

# Criação da engine
engine = create_engine(DATABASE_URL, connect_args = {"check_same_thread": False})

# Criação da sessão
Session = sessionmaker(bind = engine)

# Base para criação das classes (tabelas)
Base = declarative_base()

# Importa os modelos para garantir que sejam registrados no SQLAlchemy
from model.pet import Pet # -> Quando criamos o arquivo pet.py na pasta model

# Cria as tabelas no banco de dados, caso não existam
Base.metadata.create_all(engine)