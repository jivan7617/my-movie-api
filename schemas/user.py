from pydantic import BaseModel

#creo la clase para hacer las validaciones hereda de (baseModel)
class User(BaseModel):
    email: str
    password: str
    