
from fastapi import FastAPI,Path,Query,APIRouter ##se puede agregar body para porder utilizar la funcion, pero es mejor hacer un modelo
from typing import List ##se puede agregar optional para hacer un parametro opcional
from fastapi.responses import JSONResponse
from src.models.model import *

producto_router= APIRouter()


productos: List[Producto] =[]


@producto_router.get('/', tags=['Productos'], status_code=200, response_description='nos debe dar una respuesta existosa')
def todosProductos() -> List[Producto]:
    content=[producto.model_dump() for producto in productos]
    return JSONResponse(content=content, status_code=200)

@producto_router.get('/{id}', tags=['Productos'])
def listarProducto(id: int = Path(gt=0))-> Producto | dict:
    for a in productos:
        if a.id == id:
            return JSONResponse(content=a.model_dump(), status_code=200)
    return JSONResponse(content={}, status_code=404)

@producto_router.get('/categoria', tags=['Productos'])
def listarCategoria(categoria:str=Query(min_length=5, max_length=20))-> Producto | dict:
    for a in productos:
        if a.categoria == categoria:
            return JSONResponse(content=a.model_dump(), status_code=200)
    return JSONResponse(content={}, status_code=404)

@producto_router.post('/', tags=['Productos'])
def crearProducto(producto:ProductoCreate)-> List[Producto]:
    productos.append(producto)
    content=[producto.model_dump() for producto in productos]
    return JSONResponse(content=content, status_code=201) 

@producto_router.put('/{id}', tags=['Productos'])
def actualizarProductos(id:int, producto: ProductoUpdate)->List[Producto]:
    for a in productos:
        if a.id == id:
            a.nombre= producto.nombre
            a.marca= producto.marca
            a.descripcion= producto.descripcion
            a.categoria= producto.categoria
            a.ano= producto.ano
            a.precio= producto.precio
    content=[producto.model_dump() for producto in productos]
    return JSONResponse(content=content, status_code=200) 


@producto_router.delete('/{id}', tags=['Productos'])
def eliminarProducto(id:int)->List[Producto]:
    for a in productos:
        if a.id == id:
            productos.remove(a)
    content=[producto.model_dump() for producto in productos]
    return JSONResponse(content=content, status_code=200) 