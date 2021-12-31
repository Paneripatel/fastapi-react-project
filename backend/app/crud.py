from sqlalchemy.orm import Session
from . import models

def get_user(db: Session, user: dict):
    return db.query(models.User).filter(models.User.email == user.get('email'), models.User.hashed_password == user.get('hashed_password')).first()

def create_user(db: Session, user: dict):
    db_user = models.User(email=user.get('email'), hashed_password=user.get('hashed_password'))
    db.add(db_user)
    db.commit()    
    db.refresh(db_user)
    return db_user

def add_my_pokemon(db: Session, mypokemon: dict):
    user = db.query(models.User).filter(models.User.email == mypokemon.get('email')).first()
    user_id = 0
    if user is not None:
        user_id = user.id

    db_mypokemon = models.MyPokemon(pokemon_name = mypokemon.get('pokemon_name'), user_id=user_id)
    db.add(db_mypokemon)
    db.commit()
    db.refresh(db_mypokemon)
    return db_mypokemon

def get_my_pokemon(db: Session, user: dict):
    user = db.query(models.User).filter(models.User.email == user.get('email')).first()
    if user is not None:
        my_pokemons = db.query(models.MyPokemon).filter(models.MyPokemon.user_id == user.id).all()
        return my_pokemons
    else:
        return None