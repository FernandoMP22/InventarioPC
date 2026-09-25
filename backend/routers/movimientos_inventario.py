# ==========================================
# MOVIMIENTO_INVENTARIO
# ==========================================

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.database.movimientos_inventario import obtener_movimientos_inventario as obtener_movimientos_inventario_db
from backend.database.movimientos_inventario import obtener_movimiento_inventario as obtener_movimiento_inventario_db
from backend.database.movimientos_inventario import crear_movimiento_inventario as crear_movimiento_inventario_db
from backend.database.movimientos_inventario import actualizar_movimiento_inventario as actualizar_movimiento_inventario_db
from backend.database.movimientos_inventario import eliminar_movimiento_inventario as eliminar_movimiento_inventario_db


router = APIRouter()


class MovimientoInventario(BaseModel):
    id_producto: int
    tipo_movimiento: str
    cantidad: int
    fecha: str
    motivo: str


@router.get("/movimientos-inventario")
def obtener_movimientos_inventario(db: Session = Depends(get_db)):
    return obtener_movimientos_inventario_db(db)


@router.get("/movimientos-inventario/{id}")
def obtener_movimiento_inventario(id: int, db: Session = Depends(get_db)):
    movimiento = obtener_movimiento_inventario_db(id, db)

    if movimiento is None:
        raise HTTPException(
            status_code=404,
            detail="Movimiento de inventario no encontrado"
        )

    return movimiento


@router.post("/movimientos-inventario")
def crear_movimiento_inventario(movimiento: MovimientoInventario, db: Session = Depends(get_db)):
    resultado = crear_movimiento_inventario_db(movimiento, db)

    if resultado is False:
        raise HTTPException(
            status_code=400,
            detail="No se pudo crear el movimiento de inventario"
        )

    return {"mensaje": "Movimiento de inventario creado correctamente"}


@router.put("/movimientos-inventario/{id}")
def actualizar_movimiento_inventario(
    id: int,
    movimiento: MovimientoInventario,
    db: Session = Depends(get_db)
):
    resultado = actualizar_movimiento_inventario_db(
        id,
        movimiento,
        db
    )

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Movimiento de inventario no encontrado"
        )

    return {"mensaje": "Movimiento de inventario actualizado correctamente"}


@router.delete("/movimientos-inventario/{id}")
def eliminar_movimiento_inventario(id: int, db: Session = Depends(get_db)):
    resultado = eliminar_movimiento_inventario_db(id, db)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Movimiento de inventario no encontrado"
        )

    return {"mensaje": "Movimiento de inventario eliminado correctamente"}
