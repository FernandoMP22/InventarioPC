# ==========================================
# CLIENTE
# ==========================================

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database.session import get_db

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
def obtener_clientes(db: Session = Depends(get_db)):
    return obtener_clientes_db(db)


@router.get("/clientes/{id}")
def obtener_cliente(id: int, db: Session = Depends(get_db)):
    cliente = obtener_cliente_db(id, db)

    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    return cliente


@router.post("/clientes")
def crear_cliente(cliente: Cliente, db: Session = Depends(get_db)):
    resultado = crear_cliente_db(cliente, db)

    if resultado is False:
        raise HTTPException(
            status_code=400,
            detail="No se pudo crear el cliente"
        )

    return {"mensaje": "Cliente creado correctamente"}


@router.put("/clientes/{id}")
def actualizar_cliente(id: int, cliente: Cliente, db: Session = Depends(get_db)):
    resultado = actualizar_cliente_db(id, cliente, db)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    return {"mensaje": "Cliente actualizado correctamente"}


@router.delete("/clientes/{id}")
def eliminar_cliente(id: int, db: Session = Depends(get_db)):
    resultado = eliminar_cliente_db(id, db)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )

    return {"mensaje": "Cliente eliminado correctamente"}
