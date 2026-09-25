# ==========================================
# PRODUCTO_PROVEEDOR
# ==========================================

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.database.productos_proveedores import obtener_productos_proveedores as obtener_productos_proveedores_db
from backend.database.productos_proveedores import obtener_producto_proveedor as obtener_producto_proveedor_db
from backend.database.productos_proveedores import crear_producto_proveedor as crear_producto_proveedor_db
from backend.database.productos_proveedores import actualizar_producto_proveedor as actualizar_producto_proveedor_db
from backend.database.productos_proveedores import eliminar_producto_proveedor as eliminar_producto_proveedor_db


router = APIRouter()


class ProductoProveedor(BaseModel):
    id_producto: int
    id_proveedor: int
    costo_proveedor: float
    codigo_proveedor: str


@router.get("/productos-proveedores")
def obtener_productos_proveedores():
    return obtener_productos_proveedores_db()


@router.get("/productos-proveedores/{id_producto}/{id_proveedor}")
def obtener_producto_proveedor(id_producto: int, id_proveedor: int):
    producto_proveedor = obtener_producto_proveedor_db(
        id_producto,
        id_proveedor
    )

    if producto_proveedor is None:
        raise HTTPException(
            status_code=404,
            detail="Relación producto-proveedor no encontrada"
        )

    return producto_proveedor


@router.post("/productos-proveedores")
def crear_producto_proveedor(producto_proveedor: ProductoProveedor):
    resultado = crear_producto_proveedor_db(producto_proveedor)

    if resultado is False:
        raise HTTPException(
            status_code=400,
            detail="No se pudo crear la relación producto-proveedor"
        )

    return {"mensaje": "Relación producto-proveedor creada correctamente"}


@router.put("/productos-proveedores/{id_producto}/{id_proveedor}")
def actualizar_producto_proveedor(
    id_producto: int,
    id_proveedor: int,
    producto_proveedor: ProductoProveedor
):
    resultado = actualizar_producto_proveedor_db(
        id_producto,
        id_proveedor,
        producto_proveedor
    )

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Relación producto-proveedor no encontrada"
        )

    return {"mensaje": "Relación producto-proveedor actualizada correctamente"}


@router.delete("/productos-proveedores/{id_producto}/{id_proveedor}")
def eliminar_producto_proveedor(id_producto: int, id_proveedor: int):
    resultado = eliminar_producto_proveedor_db(
        id_producto,
        id_proveedor
    )

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Relación producto-proveedor no encontrada"
        )

    return {"mensaje": "Relación producto-proveedor eliminada correctamente"}