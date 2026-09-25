from sqlalchemy import select

from backend.models import Proveedor


def obtener_proveedores(session):
    consulta = select(Proveedor)

    resultado = session.execute(consulta)

    return resultado.scalars().all()



def obtener_proveedor(id_proveedor, session):
    consulta = select(Proveedor).where(
        Proveedor.id_proveedor == id_proveedor
    )

    resultado = session.execute(consulta)

    return resultado.scalars().first()



def crear_proveedor(proveedor, session):
    try:
        nuevo_proveedor = Proveedor(
            nombre=proveedor.nombre,
            telefono=proveedor.telefono,
            correo=proveedor.correo,
            direccion=proveedor.direccion
        )

        session.add(nuevo_proveedor)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False



def actualizar_proveedor(id_proveedor, proveedor, session):
    try:
        consulta = select(Proveedor).where(
            Proveedor.id_proveedor == id_proveedor
        )

        proveedor_db = session.execute(
            consulta
        ).scalars().first()

        if proveedor_db is None:
            return False

        proveedor_db.nombre = proveedor.nombre
        proveedor_db.telefono = proveedor.telefono
        proveedor_db.correo = proveedor.correo
        proveedor_db.direccion = proveedor.direccion

        session.commit()

        return True

    except Exception:
        session.rollback()
        return False



def eliminar_proveedor(id_proveedor, session):
    try:
        consulta = select(Proveedor).where(
            Proveedor.id_proveedor == id_proveedor
        )

        proveedor = session.execute(
            consulta
        ).scalars().first()

        if proveedor is None:
            return False

        session.delete(proveedor)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False
