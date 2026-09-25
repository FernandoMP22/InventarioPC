from sqlalchemy import select

from backend.models import Categoria


def obtener_categorias(session):
    consulta = select(Categoria)

    resultado = session.execute(consulta)

    return resultado.scalars().all()



def obtener_categoria(id_categoria, session):
    consulta = select(Categoria).where(
        Categoria.id_categoria == id_categoria
    )

    resultado = session.execute(consulta)

    return resultado.scalars().first()



def crear_categoria(categoria, session):
    try:
        nueva_categoria = Categoria(
            nombre=categoria.nombre,
            descripcion=categoria.descripcion
        )

        session.add(nueva_categoria)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False



def actualizar_categoria(id_categoria, categoria, session):
    try:
        consulta = select(Categoria).where(
            Categoria.id_categoria == id_categoria
        )

        categoria_db = session.execute(
            consulta
        ).scalars().first()

        if categoria_db is None:
            return False

        categoria_db.nombre = categoria.nombre
        categoria_db.descripcion = categoria.descripcion

        session.commit()

        return True

    except Exception:
        session.rollback()
        return False



def eliminar_categoria(id_categoria, session):
    try:
        consulta = select(Categoria).where(
            Categoria.id_categoria == id_categoria
        )

        categoria = session.execute(
            consulta
        ).scalars().first()

        if categoria is None:
            return False

        session.delete(categoria)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False
