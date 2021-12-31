from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    my_pokemons = relationship("MyPokemon", back_populates="user")

class MyPokemon(Base):
    __tablename__ = "mypokemons"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    pokemon_name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="my_pokemons")