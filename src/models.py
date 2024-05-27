import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    personaje_favorito = relationship("Personaje_Favorito", back_populates="usuario")
    planeta_favorito = relationship("Planeta_Favorito", back_populates="usuario")
    nave_favorito = relationship("Nave_Favorito", back_populates="usuario")


class Personaje(Base):
    
    __tablename__ = 'Personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    height = Column(Float, nullable=False)
    gender = Column(String(250), nullable=False)

    personaje_favorito = relationship("Personaje_Favorito", back_populates="personaje")

class Personaje_Favorito(Base):
    __tablename__ = "Personaje_Favorito"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("Usuario.id"))
    personaje_id = Column(Integer, ForeignKey("Personaje.id"))

    usuario = relationship("Usuario", back_populates="personaje_favorito")
    personaje = relationship("Personaje", back_populates="personaje_favorito")

class Planeta(Base):    
    __tablename__ = 'Planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    diameter = Column(Float, nullable=False)

    planeta_favorito = relationship("Planeta_Favorito", back_populates="planeta")

class Planeta_Favorito(Base):
    __tablename__ = "Planeta_Favorito"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("Usuario.id"))
    planeta_id = Column(Integer, ForeignKey("Planeta.id"))
    
    usuario = relationship("Usuario", back_populates="personaje_favorito")
    planeta = relationship("Planeta", back_populates="planeta_favorito")

class Nave(Base):    
    __tablename__ = 'Nave'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    starship_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    passengers = Column(Float, nullable=False)
    length = Column(Float, nullable=False)

    nave_favorito = relationship("Nave_Favorito", back_populates="nave")

class Nave_Favorito(Base):
    __tablename__ = "Nave_Favorito"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("Usuario.id"))
    nave_id = Column(Integer, ForeignKey("Nave.id"))
    
    usuario = relationship("Usuario", back_populates="personaje_favorito")
    nave = relationship("Nave", back_populates="nave_favorito")

## Dibuja desde la base de datos SQLAlchemy
render_er(Base, 'diagram.png')