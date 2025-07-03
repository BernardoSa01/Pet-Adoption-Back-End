from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model import Base

class Pet(Base):
  __tablename__ = 'pet'

  id = Column(Integer, primary_key = True, autoincrement = True)
  nome = Column(String(100))
  especie = Column(String(50), nullable = False)
  raca = Column(String(50), nullable = False)
  idade = Column(Integer, nullable = False)
  sexo = Column(String(20), nullable = False)
  descricao = Column(String(300), nullable = True)

  def __init__(self, nome: str, especie: str, raca: str, idade: int, sexo: str, descricao: str = None):
    """
    Cria um Pet
    
    Parâmetros:
        nome: Nome do pet
        especie: Espécie (cachorro, gato, etc.)
        raca: Raça do pet
        idade: Idade do pet
        sexo: Sexo do pet
        descricao: Descrição adicional
    """

    self.nome = nome
    self.especie = especie
    self.raca = raca
    self.idade = idade
    self.sexo = sexo
    self.descricao = descricao

  def __repr__(self): 
    return f"<Pet(nome={self.nome}, especie={self.especie}, raca={self.raca})>"