from pydantic import BaseModel, Field
from typing import Optional,List
import datetime

class Producto(BaseModel):
    id: int
    nombre:str
    marca:str
    descripcion: str
    categoria: str
    ano:int
    precio: float

class ProductoUpdate(BaseModel):
    nombre:str
    marca:str
    descripcion: str
    categoria: str
    ano:int
    precio: float 

class ProductoCreate(BaseModel):
    id: int 
    nombre:str=Field(min_length=5, max_length=30) #default="sin nombre")
    marca:str=Field(min_length=2, max_length=15) #default="sin nombre")
    descripcion: str=Field(min_length=15, max_length=50) #default="sin descripcion")
    categoria: str
    ano:int=Field(le=datetime.date.today().year, ge=1900) #default=1900)
    precio: float    

    model_config = {
        'json_schema_extra':{
            'example':{
                "id":1,
                "nombre":"nombre herramienta",
                "marca":"marca",
                "descripcion":"esto sirve para ...",
                "categoria":"categoria",
                "ano":1900,
                "precio":0
            }
            
        }
    }

# gt greater than
# ge greater than or equal
# lt less than
# le less than or equal