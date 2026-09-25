# ==========================================
# PRODUCTO
# ==========================================

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.database.productos import obtener_productos as obtener_productos_db
from backend.database.productos import obtener_producto as obtener_producto_db
from backend.database.productos import crear_producto as crear_producto_db
from backend.database.productos import actualizar_producto as actualizar_producto_db
from backend.database.productos import eliminar_producto as eliminar_producto_db

router = APIRouter()


class Producto(BaseModel):
    nombre: str
    marca: str
    modelo: str
    precio_compra: float
    precio_venta: float
    stock_actual: int
    stock_minimo: int
    id_categoria: int

@router.get("/productos")
def obtener_productos():
    productos = obtener_productos_db()

    if productos is None:
        raise HTTPException(
            status_code=404,
            detail="No se encontraron productos"
        )

    return productos


@router.get("/productos/{id_producto}")
def obtener_producto(id_producto: int):
    producto = obtener_producto_db(id_producto)

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return producto


@router.post("/productos")
def crear_producto(producto: Producto):
    resultado = crear_producto_db(producto)

    if resultado is False:
        raise HTTPException(
            status_code=400,
            detail="No se pudo crear el producto"
        )

    return {"mensaje": "Producto creado correctamente"}


@router.put("/productos/{id_producto}")
def actualizar_producto(id_producto: int, producto: Producto):
    resultado = actualizar_producto_db(id_producto, producto)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return {"mensaje": "Producto actualizado correctamente"}


@router.delete("/productos/{id_producto}")
def eliminar_producto(id_producto: int):
    resultado = eliminar_producto_db(id_producto)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return {"mensaje": "Producto eliminado correctamente"}