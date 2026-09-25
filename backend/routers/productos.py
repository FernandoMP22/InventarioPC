# ==========================================
# PRODUCTO
# ==========================================

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database.session import get_db

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
def obtener_productos(db: Session = Depends(get_db)):
    productos = obtener_productos_db(db)

    if productos is None:
        raise HTTPException(
            status_code=404,
            detail="No se encontraron productos"
        )

    return productos


@router.get("/productos/{id_producto}")
def obtener_producto(id_producto: int, db: Session = Depends(get_db)):
    producto = obtener_producto_db(id_producto, db)

    if producto is None:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return producto


@router.post("/productos")
def crear_producto(producto: Producto, db: Session = Depends(get_db)):
    resultado = crear_producto_db(producto, db)

    if resultado is False:
        raise HTTPException(
            status_code=400,
            detail="No se pudo crear el producto"
        )

    return {"mensaje": "Producto creado correctamente"}


@router.put("/productos/{id_producto}")
def actualizar_producto(
    id_producto: int,
    producto: Producto,
    db: Session = Depends(get_db)
):
    resultado = actualizar_producto_db(id_producto, producto, db)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return {"mensaje": "Producto actualizado correctamente"}


@router.delete("/productos/{id_producto}")
def eliminar_producto(id_producto: int, db: Session = Depends(get_db)):
    resultado = eliminar_producto_db(id_producto, db)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Producto no encontrado"
        )

    return {"mensaje": "Producto eliminado correctamente"}
