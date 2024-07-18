from jwt import encode, decode

#nombre funcion:(tipo diccionario):
#nombre variable: str = payload(contenido= data, clave, algoritmo para generar el token)
def create_token(data: dict) -> str:
    token: str = encode(payload=data, key="secrete_key_1234", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key= "secrete_key_1234", algorithms=["HS256"])
    return data


