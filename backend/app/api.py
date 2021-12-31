from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, crud
from .database import SessionLocal, engine


import requests
import json

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

user_fav_pokemon = [{
            "name": "bulbasaur",
            "url": "https://pokeapi.co/api/v2/pokemon/1/"
        }]


@app.get("/pokemon", tags=["pokemons"])
async def read_root() -> dict:
    pokemon_url = "https://pokeapi.co/api/v2/pokemon?limit=20&offset=0"
    pokemon_response = requests.get(pokemon_url)
    if pokemon_response.status_code == 200:
        results = json.loads(pokemon_response.content.decode('utf-8'))
        return results["results"]
    return {"message": "Error"}


@app.post("/fav_pokemon", tags=["pokemons"])
async def add_fav(pokemon: dict, db: Session = Depends(get_db)) -> dict:
    my_pokemon = crud.add_my_pokemon(db, mypokemon=pokemon)
    return {
        "data" : {"Pokemon Added."}
    }

@app.post("/get_fav_pokemon", tags=["pokemons"])
async def fav_pokemon(user: dict, db: Session= Depends(get_db)) -> dict:
    return crud.get_my_pokemon(db, user)

@app.get("/user")
async def get_user(user: dict, db: Session= Depends(get_db)) -> dict:
    returnuser = crud.get_user(db, user= user)
    if returnuser is None:
        return {"result":"false"}
    else:
        return returnuser


@app.post("/user")
async def insert_user(user:dict, db: Session= Depends(get_db)) -> dict:
    return crud.create_user(db, user= user)