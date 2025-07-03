from pydantic import BaseModel
from typing import List, Optional

class PetSchema(BaseModel):
  """ Define como um novo pet deve ser cadastrado """
  nome: str
  especie: str
  raca: str
  idade: int
  sexo: str
  descricao: Optional[str] = None

class PetBuscaSchema(BaseModel): 
  """ Define como deve ser a estrutura para buscar um pet pelo nome """
  nome: str


class PetBuscaIdSchema(BaseModel):
  """Define como deve ser a busca de um pet pelo id"""
  id: int 

class PetViewSchema(BaseModel):
  """ Define como um pet será retornado na busca """
  id: int
  nome: str
  especie: str
  raca: str
  idade: int
  sexo: str
  descricao: Optional[str] = None

class ListagemPetsSchema(BaseModel):
  """ Define como uma listagem de pets será retornada """
  pets: List[PetViewSchema]

class PetDelSchema(BaseModel): 
  """ Define os dados retornados após uma remoção """
  message: str
  id: int


class PetsListSchema(BaseModel):
    pets: List[PetViewSchema]


def apresenta_pet(pet):
  """ Retorna uma representação do pet """
  return {
    "id": pet.id,
    "nome": pet.nome,
    "especie": pet.especie,
    "raca": pet.raca,
    "idade": pet.idade,
    "sexo": pet.sexo,
    "descricao": pet.descricao
  }


def apresenta_pets(pets): 
  """ Retorna uma representação da listagem de pets """
  result = []
  for pet in pets: 
    result.append({
      "id": pet.id,
      "nome": pet.nome,
      "especie": pet.especie,
      "raca": pet.raca,
      "idade": pet.idade,
      "sexo": pet.sexo,
      "descricao": pet.descricao
    })
  return {"pets": result}



def apresenta_pets_lista(pets): 
  """Retorna uma lista pura de pets, sem dicionário agrupador"""
  return [
    {
      "id": pet.id,
      "nome": pet.nome,
      "especie": pet.especie,
      "raca": pet.raca,
      "idade": pet.idade,
      "sexo": pet.sexo,
      "descricao": pet.descricao
    } for pet in pets
  ]
