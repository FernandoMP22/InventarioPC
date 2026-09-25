from datetime import date

from sqlalchemy import select

from backend.models import Devolucion


def obtener_devoluciones(session):
    consulta = select(Devolucion)

    resultado = session.execute(consulta)

    return resultado.scalars().all()



def obtener_devolucion(id_devolucion, session):
    consulta = select(Devolucion).where(
        Devolucion.id_devolucion == id_devolucion
    )

    resultado = session.execute(consulta)

    return resultado.scalars().first()



def crear_devolucion(devolucion, session):
    try:
        nueva_devolucion = Devolucion(
            id_detalle=devolucion.id_detalle,
            fecha_devolucion=date.fromisoformat(
                devolucion.fecha_devolucion
            ),
            cantidad=devolucion.cantidad,
            motivo=devolucion.motivo,
            estado=devolucion.estado
        )

        session.add(nueva_devolucion)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False



def actualizar_devolucion(id_devolucion, devolucion, session):
    try:
        consulta = select(Devolucion).where(
            Devolucion.id_devolucion == id_devolucion
        )

        devolucion_db = session.execute(
            consulta
        ).scalars().first()

        if devolucion_db is None:
            return False

        devolucion_db.id_detalle = devolucion.id_detalle
        devolucion_db.fecha_devolucion = date.fromisoformat(
            devolucion.fecha_devolucion
        )
        devolucion_db.cantidad = devolucion.cantidad
        devolucion_db.motivo = devolucion.motivo
        devolucion_db.estado = devolucion.estado

        session.commit()

        return True

    except Exception:
        session.rollback()
        return False



def eliminar_devolucion(id_devolucion, session):
    try:
        consulta = select(Devolucion).where(
            Devolucion.id_devolucion == id_devolucion
        )

        devolucion = session.execute(
            consulta
        ).scalars().first()

        if devolucion is None:
            return False

        session.delete(devolucion)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False
