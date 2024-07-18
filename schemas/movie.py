from pydantic import BaseModel, Field
from typing import Optional

# class persona hereda de (BaseModel)
class Movie(BaseModel):
    #id: int | None = None no admite repetidos unicco autoincremental
    id: Optional[int] = None
    
    # defauld (texto de ejemplo), Field ( las validaciones deseadas)
    title: str = Field(max_length=35)
    overview: str = Field(max_length= 350)
    #solo peliculas menores (less <= 2000)
    year: int = Field(le=2000)
    # (>1 | < 10) ge, le
    rating: float = Field(ge=1, le=10)
    category: str = Field(max_length=30)
    
    #atributo orm para permitir la numeracion del id en serie
    class Config:
        #orm_mode = True,
        json_schema_extra = {
            "example": {           
                "title": "Titulo solo clasicos",
                "overview": "Descrive la pelicula",
                "year": 2000,
                "rating": 7.8,
                "category": "accion"  
            }
        }