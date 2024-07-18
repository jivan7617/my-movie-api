from fastapi import  FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

#crear la instancia de la aplicacion 
app = FastAPI()
# titulo en el navegador
app.title = "esta en una gran APP" 
# para colocar la version de mi app
app.version = "0.0.1"
# hacer validacion de errores con(ErrorHandler)
app.add_middleware(ErrorHandler)
# llamar al router desde (movie_router)
app.include_router(movie_router)
# llamar al router desde (user_router)
app.include_router(user_router)

#from config.database llamo a la base de datos y le paso engine el motor de busqueda
Base.metadata.create_all(bind=engine)
    
movies =    [
                {
                "id": 1,
                "category": "suspenso",
                "title": "avatares",
                "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
                "year": "1999",
                "rating": 6.8
                }
                
            ]

# metodo get
# crear la ruta de inicio CON EL NOMBRE (home)
@app.get('/', tags=['Home'])
def message():
    return HTMLResponse("<h1>bienvenido a mi app<h1>")




