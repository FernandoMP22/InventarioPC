# ==========================================
# CLIENTE
# ==========================================

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.database.clientes import obtener_clientes as obtener_clientes_db
from backend.database.clientes import obtener_cliente as obtener_cliente_db
from backend.database.clientes import crear_cliente as crear_cliente_db
from backend.database.clientes import actualizar_cliente as actualizar_cliente_db
from backend.database.clientes import eliminar_cliente as eliminar_cliente_db


router = APIRouter()


class Cliente(BaseModel):
    nombre: str
    apellido: str
    telefono: str | None = None
    correo: str | None = None


@router.get("/clientes")
def obtener_clientes():
    return obtener_clientes_db()


@router.get("/clientes/{id}")
def obtener_cliente(id: int):
    cliente = obtener_cliente_db(id)

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    return cliente


@router.post("/clientes")
def crear_cliente(cliente: Cliente):
    resultado = crear_cliente_db(cliente)

    if resultado is False:
        raise HTTPException(
            status_code=400,
            detail="No se pudo crear el cliente"
        )

    return {"mensaje": "Cliente creado correctamente"}


@router.put("/clientes/{id}")
def actualizar_cliente(id: int, cliente: Cliente):
    resultado = actualizar_cliente_db(id, cliente)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    return {"mensaje": "Cliente actualizado correctamente"}


@router.delete("/clientes/{id}")
def eliminar_cliente(id: int):
    resultado = eliminar_cliente_db(id)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    return {"mensaje": "Cliente eliminado correctamente"}