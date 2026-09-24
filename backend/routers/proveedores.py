# ==========================================
# PROVEEDOR
# ==========================================

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from database.proveedores import obtener_proveedores as obtener_proveedores_db
from database.proveedores import obtener_proveedor as obtener_proveedor_db
from database.proveedores import crear_proveedor as crear_proveedor_db
from database.proveedores import actualizar_proveedor as actualizar_proveedor_db
from database.proveedores import eliminar_proveedor as eliminar_proveedor_db


router = APIRouter()


class Proveedor(BaseModel):
    nombre: str
    telefono: str
    correo: str
    direccion: str


@router.get("/proveedores")
def obtener_proveedores():
    return obtener_proveedores_db()


@router.get("/proveedores/{id}")
def obtener_proveedor(id: int):
    proveedor = obtener_proveedor_db(id)

    if proveedor is None:
        raise HTTPException(
            status_code=404,
            detail="Proveedor no encontrado"
        )

    return proveedor


@router.post("/proveedores")
def crear_proveedor(proveedor: Proveedor):
    resultado = crear_proveedor_db(proveedor)

    if resultado is False:
        raise HTTPException(
            status_code=400,
            detail="No se pudo crear el proveedor"
        )

    return {"mensaje": "Proveedor creado correctamente"}


@router.put("/proveedores/{id}")
def actualizar_proveedor(id: int, proveedor: Proveedor):
    resultado = actualizar_proveedor_db(id, proveedor)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Proveedor no encontrado"
        )

    return {"mensaje": "Proveedor actualizado correctamente"}


@router.delete("/proveedores/{id}")
def eliminar_proveedor(id: int):
    resultado = eliminar_proveedor_db(id)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Proveedor no encontrado"
        )

    return {"mensaje": "Proveedor eliminado correctamente"}