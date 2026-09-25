# ==========================================
# DEVOLUCION
# ==========================================

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.database.devoluciones import obtener_devoluciones as obtener_devoluciones_db
from backend.database.devoluciones import obtener_devolucion as obtener_devolucion_db
from backend.database.devoluciones import crear_devolucion as crear_devolucion_db
from backend.database.devoluciones import actualizar_devolucion as actualizar_devolucion_db
from backend.database.devoluciones import eliminar_devolucion as eliminar_devolucion_db


router = APIRouter()


class Devolucion(BaseModel):
    id_detalle: int
    fecha_devolucion: str
    cantidad: int
    motivo: str
    estado: str


@router.get("/devoluciones")
def obtener_devoluciones():
    return obtener_devoluciones_db()


@router.get("/devoluciones/{id}")
def obtener_devolucion(id: int):
    devolucion = obtener_devolucion_db(id)

    if devolucion is None:
        raise HTTPException(
            status_code=404,
            detail="Devolucion no encontrada"
        )

    return devolucion


@router.post("/devoluciones")
def crear_devolucion(devolucion: Devolucion):
    resultado = crear_devolucion_db(devolucion)

    if resultado is False:
        raise HTTPException(
            status_code=400,
            detail="No se pudo crear la devolucion"
        )

    return {"mensaje": "Devolucion creada correctamente"}


@router.put("/devoluciones/{id}")
def actualizar_devolucion(id: int, devolucion: Devolucion):
    resultado = actualizar_devolucion_db(id, devolucion)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Devolucion no encontrada"
        )

    return {"mensaje": "Devolucion actualizada correctamente"}


@router.delete("/devoluciones/{id}")
def eliminar_devolucion(id: int):
    resultado = eliminar_devolucion_db(id)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Devolucion no encontrada"
        )

    return {"mensaje": "Devolucion eliminada correctamente"}