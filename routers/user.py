
from fastapi import APIRouter
from utils.jwt_manager import create_token
from fastapi.responses import JSONResponse
from schemas.user import User

#creo el router
user_router = APIRouter()


# hacer validacion con email
@user_router.post('/login', tags=['auth'])
def login(user:User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        #llamo la funcion para crear el token
        token: str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)