#importar desde mi configuracion
from config.database import Base 
from sqlalchemy import Column, Integer, Float, String

#creo la clase que va a ser la entidad movie que hereda de Base
class Movie (Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key = True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)