from datetime import date

from sqlalchemy import select

from backend.database.session import SessionLocal
from backend.models import MovimientoInventario


def obtener_movimientos_inventario():
    session = SessionLocal()

    try:
        consulta = select(MovimientoInventario)

        resultado = session.execute(consulta)

        return resultado.scalars().all()

    finally:
        session.close()


def obtener_movimiento_inventario(id_movimiento):
    session = SessionLocal()

    try:
        consulta = select(MovimientoInventario).where(
            MovimientoInventario.id_movimiento == id_movimiento
        )

        resultado = session.execute(consulta)

        return resultado.scalars().first()

    finally:
        session.close()


def crear_movimiento_inventario(movimiento):
    session = SessionLocal()

    try:
        nuevo_movimiento = MovimientoInventario(
            id_producto=movimiento.id_producto,
            tipo_movimiento=movimiento.tipo_movimiento,
            cantidad=movimiento.cantidad,
            fecha=date.fromisoformat(movimiento.fecha),
            motivo=movimiento.motivo
        )

        session.add(nuevo_movimiento)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False

    finally:
        session.close()


def actualizar_movimiento_inventario(
    id_movimiento,
    movimiento
):
    session = SessionLocal()

    try:
        consulta = select(MovimientoInventario).where(
            MovimientoInventario.id_movimiento == id_movimiento
        )

        movimiento_db = session.execute(
            consulta
        ).scalars().first()

        if movimiento_db is None:
            return False

        movimiento_db.id_producto = movimiento.id_producto
        movimiento_db.tipo_movimiento = movimiento.tipo_movimiento
        movimiento_db.cantidad = movimiento.cantidad
        movimiento_db.fecha = date.fromisoformat(
            movimiento.fecha
        )
        movimiento_db.motivo = movimiento.motivo

        session.commit()

        return True

    except Exception:
        session.rollback()
        return False

    finally:
        session.close()


def eliminar_movimiento_inventario(id_movimiento):
    session = SessionLocal()

    try:
        consulta = select(MovimientoInventario).where(
            MovimientoInventario.id_movimiento == id_movimiento
        )

        movimiento = session.execute(
            consulta
        ).scalars().first()

        if movimiento is None:
            return False

        session.delete(movimiento)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False

    finally:
        session.close()