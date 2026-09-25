# ==========================================
# PEDIDO
# ==========================================

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.database.pedidos import obtener_pedidos as obtener_pedidos_db
from backend.database.pedidos import obtener_pedido as obtener_pedido_db
from backend.database.pedidos import crear_pedido as crear_pedido_db
from backend.database.pedidos import actualizar_pedido as actualizar_pedido_db
from backend.database.pedidos import eliminar_pedido as eliminar_pedido_db


router = APIRouter()


class Pedido(BaseModel):
    id_cliente: int | None = None
    fecha_pedido: str
    tipo_envio: str
    tipo_entrega: str
    estado: str
    total: float


@router.get("/pedidos")
def obtener_pedidos():
    return obtener_pedidos_db()


@router.get("/pedidos/{id}")
def obtener_pedido(id: int):
    pedido = obtener_pedido_db(id)

    if pedido is None:
        raise HTTPException(
            status_code=404,
            detail="Pedido no encontrado"
        )

    return pedido


@router.post("/pedidos")
def crear_pedido(pedido: Pedido):
    resultado = crear_pedido_db(pedido)

    if resultado is False:
        raise HTTPException(
            status_code=400,
            detail="No se pudo crear el pedido"
        )

    return {"mensaje": "Pedido creado correctamente"}


@router.put("/pedidos/{id}")
def actualizar_pedido(id: int, pedido: Pedido):
    resultado = actualizar_pedido_db(id, pedido)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Pedido no encontrado"
        )

    return {"mensaje": "Pedido actualizado correctamente"}


@router.delete("/pedidos/{id}")
def eliminar_pedido(id: int):
    resultado = eliminar_pedido_db(id)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Pedido no encontrado"
        )

    return {"mensaje": "Pedido eliminado correctamente"}