from datetime import date

from sqlalchemy import select

from backend.database.session import SessionLocal
from backend.models import Devolucion


def obtener_devoluciones():
    session = SessionLocal()

    try:
        consulta = select(Devolucion)

        resultado = session.execute(consulta)

        return resultado.scalars().all()

    finally:
        session.close()


def obtener_devolucion(id_devolucion):
    session = SessionLocal()

    try:
        consulta = select(Devolucion).where(
            Devolucion.id_devolucion == id_devolucion
        )

        resultado = session.execute(consulta)

        return resultado.scalars().first()

    finally:
        session.close()


def crear_devolucion(devolucion):
    session = SessionLocal()

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

    finally:
        session.close()


def actualizar_devolucion(id_devolucion, devolucion):
    session = SessionLocal()

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

    finally:
        session.close()


def eliminar_devolucion(id_devolucion):
    session = SessionLocal()

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

    finally:
        session.close()