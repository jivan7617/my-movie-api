from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse


#creo la clase
class ErrorHandler(BaseHTTPMiddleware):
    #con el metodo constructor que requiere una aplicacion (FastAPI)
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)
        
    #creo un metodo asincrono para ver si la aplicacion esta funcionando mal
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500, content={'error': str(e)})
    
    
    