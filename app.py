from flask_openapi3 import OpenAPI, Info, Tag 
from flask import redirect, request 
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError, SQLAlchemyError


from model import Session, Pet
from logger import logger
from schemas import *
from flask_cors import CORS
from typing import List


# Definindo título e versão da API
info = Info(title = "Pet Adoption API", version = "1.0.0")
app = OpenAPI(__name__, info = info)
CORS(app)

# Definindo as tags para documentação
home_tag = Tag(name = "Documentação", description = "Documentação da API: Swagger, Redoc ou RapiDoc")
pet_tag = Tag(name = "Pet", description = "Cadastro, visualização e remoção de pets para adoção")


# Rotas

# Rota raiz, redireciona para a documentação
@app.get('/', tags = [home_tag])
def home():
  """Redireciona para a documentação interativa da API"""
  return redirect('/openapi')


# POST - Cadastrar um pet
@app.post('/pet', tags = [pet_tag],
          responses = {"200": PetViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_pet(body: PetSchema):
  """ Adiciona um novo pet à base de dados."""
  pet = Pet(
    nome = body.nome,
    especie = body.especie,
    raca = body.raca,
    idade = body.idade,
    sexo = body.sexo,
    descricao = body.descricao
  )

  logger.debug(f"Adicionando pet: '{pet.nome}'")

  try: 
    session = Session()
    session.add(pet)
    session.commit()
    logger.debug(f"Pet adicionado: '{pet.nome}'")
    return apresenta_pet(pet), 200

  except SQLAlchemyError as e:
        error_msg = "Não foi possível salvar o pet na base."
        logger.warning(f"Erro ao adicionar pet '{pet.nome}': {error_msg}")
        return {"message": error_msg}, 400


# GET - Listar todos os pets
@app.get('/pets', tags = [pet_tag],
          responses = {"200": ListagemPetsSchema, "404": ErrorSchema})
def get_pets(): 
  """ Lista todos os pets cadastrados. """
  logger.debug("Coletando pets")
  session = Session()
  pets = session.query(Pet).all()

  if not pets:
    return {"pets": []}, 200
  else: 
    logger.debug(f"{len(pets)} pets encontrados")
    return apresenta_pets(pets), 200


# GET - Buscar um pet por nome
@app.get('/pet', tags=[pet_tag],
         responses={"200": ListagemPetsSchema, "404": ErrorSchema})
def get_pet():
    """Busca pets com o nome fornecido via query string."""
    nome = request.args.get("nome")  # <-- Esse é o segredo

    if not nome:
        error_msg = "Parâmetro 'nome' não foi fornecido na query string."
        logger.warning(error_msg)
        return {"message": error_msg}, 400

    logger.debug(f"Buscando pets com nome (case-insensitive): '{nome}'")

    session = Session()
    pets = session.query(Pet).filter(Pet.nome.ilike(nome)).all()

    if not pets:
        error_msg = "Pet não encontrado na base."
        logger.warning(f"Erro ao buscar pet '{nome}': {error_msg}")
        return {"message": error_msg}, 404

    logger.debug(f"{len(pets)} pet(s) encontrado(s) com nome '{nome}'")
    return apresenta_pets(pets), 200


# DELETE - Remover um pet por nome
@app.delete('/pet', tags = [pet_tag],
            responses = {"200": PetDelSchema, "404": ErrorSchema})
def del_pet(body: PetBuscaIdSchema):
  """ Remove um pet a partir do ID informado. """
  pet_id = body.id
  logger.debug(f"Removendo pet de id: {pet_id}")
  session = Session()
  count = session.query(Pet).filter(Pet.id == pet_id).delete()
  session.commit()

  if count: 
    logger.debug(f"Pet deletado: id {pet_id}")
    return {"message": "Pet removido com sucesso!", "id": pet_id}
  else:
    error_msg = "Pet não encontrado na base"
    logger.warning(f"Erro ao deletar pet id '{pet_id}': {error_msg}")
    return {"message": error_msg}, 404
  

if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)