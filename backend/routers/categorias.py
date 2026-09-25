# ==========================================
# CATEGORIA
# ==========================================

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database.session import get_db

from backend.database.categorias import obtener_categorias as obtener_categorias_db
from backend.database.categorias import obtener_categoria as obtener_categoria_db
from backend.database.categorias import crear_categoria as crear_categoria_db
from backend.database.categorias import actualizar_categoria as actualizar_categoria_db
from backend.database.categorias import eliminar_categoria as eliminar_categoria_db


router = APIRouter()


class Categoria(BaseModel):
    nombre: str
    descripcion: str


@router.get("/categorias")
def obtener_categorias(db: Session = Depends(get_db)):
    return obtener_categorias_db(db)


@router.get("/categorias/{id}")
def obtener_categoria(id: int, db: Session = Depends(get_db)):
    categoria = obtener_categoria_db(id, db)

    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="Categoria no encontrada"
        )

    return categoria


@router.post("/categorias")
def crear_categoria(categoria: Categoria, db: Session = Depends(get_db)):
    resultado = crear_categoria_db(categoria, db)

    if resultado is False:
        raise HTTPException(
            status_code=400,
            detail="No se pudo crear la categoria"
        )

    return {"mensaje": "Categoria creada correctamente"}


@router.put("/categorias/{id}")
def actualizar_categoria(id: int, categoria: Categoria, db: Session = Depends(get_db)):
    resultado = actualizar_categoria_db(id, categoria, db)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Categoria no encontrada"
        )

    return {"mensaje": "Categoria actualizada correctamente"}


@router.delete("/categorias/{id}")
def eliminar_categoria(id: int, db: Session = Depends(get_db)):
    resultado = eliminar_categoria_db(id, db)

    if resultado is False:
        raise HTTPException(
            status_code=404,
            detail="Categoria no encontrada"
        )

    return {"mensaje": "Categoria eliminada correctamente"}
