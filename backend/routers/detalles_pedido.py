# ==========================================
# DETALLE_PEDIDO
# ==========================================

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from database.detalles_pedido import obtener_detalles_pedido as obtener_detalles_pedido_db
from database.detalles_pedido import obtener_detalle_pedido as obtener_detalle_pedido_db
from database.detalles_pedido import crear_detalle_pedido as crear_detalle_pedido_db
from database.detalles_pedido import actualizar_detalle_pedido as actualizar_detalle_pedido_db
from database.detalles_pedido import eliminar_detalle_pedido as eliminar_detalle_pedido_db


router = APIRouter()


class DetallePedido(BaseModel):
    id_pedido: int
    id_producto: int
    cantidad: int
    precio_unitario: float
    subtotal: float


@router.get("/detalles-pedido")
def obtener_detalles_pedido():
    return obtener_detalles_pedido_db()


@router.get("/detalles-pedido/{id}")
def obtener_detalle_pedido(id: int):
    detalle = obtener_detalle_pedido_db(id)

    if detalle is None:
        raise HTTPException(
            status_code=404,
            detail="Detalle de pedido no encontrado"
        )

    return detalle


@router.post("/detalles-pedido")
def crear_detalle_pedido(detalle: DetallePedido):
    resultado = crear_detalle_pedido_db(detalle)

    if resultado is False:
        raise HTTPException(
            status_code=400,
            detail="No se pudo crear el detalle de pedido"
        )

    return {"mensaje": "Detalle de pedido creado correctamente"}


@router.put("/detalles-pedido/{id}")
def actualizar_detalle_pedido(id: int, detalle: DetallePedido):
    resultado = actualizar_detalle_pedido_db(id, detalle)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Detalle de pedido no encontrado"
        )

    return {"mensaje": "Detalle de pedido actualizado correctamente"}


@router.delete("/detalles-pedido/{id}")
def eliminar_detalle_pedido(id: int):
    resultado = eliminar_detalle_pedido_db(id)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Detalle de pedido no encontrado"
        )

    return {"mensaje": "Detalle de pedido eliminado correctamente"}