from fastapi import APIRouter
from fastapi import Depends,Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()
      

# crear la ruta de la pagina 2 CON EL NOMBRE (movies)
@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    # creo la instancia de la secion (nombre dataB) para conectarme a la base de datos
    dataB = Session()
    result = MovieService(dataB).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# ruta para optener parametros por ID
@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
#validacion por el Path parametro de ruta(id >=1 and <=2000)
def get_movie_by_id(id: int = Path(ge=1, le=2000)) :
    #creo la instancia de sesion para conectarme a la base de datos
    dataB = Session()
    # llamo de Movieservices la funcion get_movie
    result = MovieService(dataB).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "contenido no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
        

# ruta para optener parametros por nombre    
@movie_router.get('/movies{name}', tags=['movies'], status_code=200)    
def get_movie_name(name:str):
    dataB = Session()
    # quiero el primer resultasdo encontrado
    result = MovieService(dataB).get_movie_by_name(name)
    if not result:
        return JSONResponse(status_code=404, content={"message": "contenido no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
    

# ruta para optener parametros por categoria    
@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200)
def get_Movies_by_category(category:str = Query(min_length=4 , max_length=15))  -> List[Movie]:
    dataB = Session()
    result = MovieService(dataB).get_movie_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
    
# metodo post para agregar valores desde el servidor
# importar BaseModel de pydentic
@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201) 
#objeto de tipo clase (usuario de tipo persona)                   
def create_Movie(movie: Movie):
    #creo la sesion para conectarme a la base de datos
    dataB = Session()
    #llamo a movie/service
    MovieService(dataB).create_movie(movie)
    return JSONResponse( status_code=201, content={"message": "pelicula registrada con exito"})

# metodo put para cambiar valores desde el servidor
@movie_router.put('/movies/{id}', tags=['movies'],response_model=dict, status_code=200)
def Update_Movie(id:int, movie: Movie) -> dict:
    dataB = Session()
    result = MovieService(dataB).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "contenido no encontrado"})
    
    MovieService(dataB).get_movie(id,movie)
    dataB.commit()
    return JSONResponse(status_code=200, content={"message": "pelicula modificada con exito"})        

# metodo put para eliminar datos desde el servidor
@movie_router.delete('/movies/{id}', tags=['movies'],response_model=dict, status_code=200)
def delete_Movie(id:int) -> dict:
    dataB = Session()
    result = dataB.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "contenido no encontrado"})
    MovieService(dataB).delete_movie(id)
    dataB.commit()
    return JSONResponse( status_code=200, content={"message": "pelicula eliminada con exito"})