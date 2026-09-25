# ==========================================
# PROVEEDOR
# ==========================================

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.database.proveedores import obtener_proveedores as obtener_proveedores_db
from backend.database.proveedores import obtener_proveedor as obtener_proveedor_db
from backend.database.proveedores import crear_proveedor as crear_proveedor_db
from backend.database.proveedores import actualizar_proveedor as actualizar_proveedor_db
from backend.database.proveedores import eliminar_proveedor as eliminar_proveedor_db


router = APIRouter()


class Proveedor(BaseModel):
    nombre: str
    telefono: str
    correo: str
    direccion: str


@router.get("/proveedores")
def obtener_proveedores(db: Session = Depends(get_db)):
    return obtener_proveedores_db(db)


@router.get("/proveedores/{id}")
def obtener_proveedor(id: int, db: Session = Depends(get_db)):
    proveedor = obtener_proveedor_db(id, db)

    if proveedor is None:
        raise HTTPException(
            status_code=404,
            detail="Proveedor no encontrado"
        )

    return proveedor


@router.post("/proveedores")
def crear_proveedor(proveedor: Proveedor, db: Session = Depends(get_db)):
    resultado = crear_proveedor_db(proveedor, db)

    if resultado is False:
        raise HTTPException(
            status_code=400,
            detail="No se pudo crear el proveedor"
        )

    return {"mensaje": "Proveedor creado correctamente"}


@router.put("/proveedores/{id}")
def actualizar_proveedor(id: int, proveedor: Proveedor, db: Session = Depends(get_db)):
    resultado = actualizar_proveedor_db(id, proveedor, db)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Proveedor no encontrado"
        )

    return {"mensaje": "Proveedor actualizado correctamente"}


@router.delete("/proveedores/{id}")
def eliminar_proveedor(id: int, db: Session = Depends(get_db)):
    resultado = eliminar_proveedor_db(id, db)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Proveedor no encontrado"
        )

    return {"mensaje": "Proveedor eliminado correctamente"}
