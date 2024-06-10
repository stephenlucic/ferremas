from fastapi import FastAPI #Path,Query ##se puede agregar body para porder utilizar la funcion, pero es mejor hacer un modelo
from fastapi.requests import Request
from typing import List ##se puede agregar optional para hacer un parametro opcional
from fastapi.responses import JSONResponse, Response
from src.utils.https_error_handler import HTTPErrorHandler
from src.routers.producto_router import producto_router


app= FastAPI()

app.add_middleware(HTTPErrorHandler)



app.title= "Ferremax"
app.version="0.0.1"

#@app.middleware('http')
#async def http_error_handler(request:Request, call_next) -> Response|JSONResponse:
#    print('Middleware is running!')
#    return await call_next(request)



@app.get('/',tags=['home'])
def home():
    return "hello world"
#productos= [{
#    "id":1,
#    "nombre":"Martillo 10'",
#    "marca":"black & becker",
#    "descripcion":"Es para golpear clavos",
#    "categoria":"Herramientas Manuales",
#    "ano":2000,
#    "precio": 5000
#},
#{
#    "id":2,
#    "nombre":"Sierra",
#    "marca":"black & becker",
#    "descripcion":"Corta madera",
#    "categoria":"Herramientas Electricas",
#    "ano":2001,
#    "precio":149990
#}
#]

app.include_router(prefix="/productos", router=producto_router)


      

