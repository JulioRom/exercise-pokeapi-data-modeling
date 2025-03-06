import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, ForeignKey, create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Tabla de Pokémon
class Pokemon(Base):
    __tablename__ = 'pokemon'
    
    pokemon_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    base_experience: Mapped[int] = mapped_column(Integer)
    height: Mapped[int] = mapped_column(Integer)
    is_default: Mapped[bool] = mapped_column(Boolean)
    game_index: Mapped[int] = mapped_column(Integer)
    version_id: Mapped[int] = mapped_column(Integer, ForeignKey('version.version_id'))
    
    # Relaciones
    abilities = relationship("PokemonAbility", back_populates="pokemon")
    types = relationship("PokemonType", back_populates="pokemon")
    moves = relationship("PokemonMove", back_populates="pokemon")
    forms = relationship("PokemonForm", back_populates="pokemon")

# Tabla de Versiones
class Version(Base):
    __tablename__ = 'version'
    
    version_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    url: Mapped[str] = mapped_column(String(255))
    version_group: Mapped[str] = mapped_column(String(100))
    
    pokemon = relationship("Pokemon", backref="version")

# Tabla de Habilidades
class Ability(Base):
    __tablename__ = 'ability'
    
    ability_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    url: Mapped[str] = mapped_column(String(255))

# Tabla intermedia de Pokémon y Habilidades
class PokemonAbility(Base):
    __tablename__ = 'pokemon_ability'
    
    pokemon_ability_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pokemon_id: Mapped[int] = mapped_column(Integer, ForeignKey('pokemon.pokemon_id'))
    ability_id: Mapped[int] = mapped_column(Integer, ForeignKey('ability.ability_id'))
    is_hidden: Mapped[bool] = mapped_column(Boolean)
    slot: Mapped[int] = mapped_column(Integer)
    
    # Relaciones
    pokemon = relationship("Pokemon", back_populates="abilities")
    ability = relationship("Ability")

# Tabla de Tipos
class Type(Base):
    __tablename__ = 'type'
    
    type_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    url: Mapped[str] = mapped_column(String(255))

# Tabla intermedia de Pokémon y Tipos
class PokemonType(Base):
    __tablename__ = 'pokemon_type'
    
    pokemon_type_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pokemon_id: Mapped[int] = mapped_column(Integer, ForeignKey('pokemon.pokemon_id'))
    type_id: Mapped[int] = mapped_column(Integer, ForeignKey('type.type_id'))
    slot: Mapped[int] = mapped_column(Integer)
    
    # Relaciones
    pokemon = relationship("Pokemon", back_populates="types")
    type = relationship("Type")

# Tabla de Movimientos
class Move(Base):
    __tablename__ = 'move'
    
    move_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    url: Mapped[str] = mapped_column(String(255))

# Tabla intermedia de Pokémon y Movimientos
class PokemonMove(Base):
    __tablename__ = 'pokemon_move'
    
    pokemon_move_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pokemon_id: Mapped[int] = mapped_column(Integer, ForeignKey('pokemon.pokemon_id'))
    move_id: Mapped[int] = mapped_column(Integer, ForeignKey('move.move_id'))
    level_learned_at: Mapped[int] = mapped_column(Integer)
    move_learn_method: Mapped[str] = mapped_column(String(100))
    
    # Relaciones
    pokemon = relationship("Pokemon", back_populates="moves")
    move = relationship("Move")

# Tabla de Formas
class Form(Base):
    __tablename__ = 'form'
    
    form_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    url: Mapped[str] = mapped_column(String(255))

# Tabla intermedia de Pokémon y Formas
class PokemonForm(Base):
    __tablename__ = 'pokemon_form'
    
    pokemon_form_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pokemon_id: Mapped[int] = mapped_column(Integer, ForeignKey('pokemon.pokemon_id'))
    form_id: Mapped[int] = mapped_column(Integer, ForeignKey('form.form_id'))
    
    # Relaciones
    pokemon = relationship("Pokemon", back_populates="forms")
    form = relationship("Form")

# Generar el diagrama de la base de datos
render_er(Base, 'diagram.png')
