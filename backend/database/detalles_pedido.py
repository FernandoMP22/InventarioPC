from sqlalchemy import select

from backend.database.session import SessionLocal
from backend.models import DetallePedido


def obtener_detalles_pedido():
    session = SessionLocal()

    try:
        consulta = select(DetallePedido)

        resultado = session.execute(consulta)

        return resultado.scalars().all()

    finally:
        session.close()


def obtener_detalle_pedido(id_detalle):
    session = SessionLocal()

    try:
        consulta = select(DetallePedido).where(
            DetallePedido.id_detalle == id_detalle
        )

        resultado = session.execute(consulta)

        return resultado.scalars().first()

    finally:
        session.close()


def crear_detalle_pedido(detalle):
    session = SessionLocal()

    try:
        nuevo_detalle = DetallePedido(
            id_pedido=detalle.id_pedido,
            id_producto=detalle.id_producto,
            cantidad=detalle.cantidad,
            precio_unitario=detalle.precio_unitario,
            subtotal=detalle.subtotal
        )

        session.add(nuevo_detalle)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False

    finally:
        session.close()


def actualizar_detalle_pedido(id_detalle, detalle):
    session = SessionLocal()

    try:
        consulta = select(DetallePedido).where(
            DetallePedido.id_detalle == id_detalle
        )

        detalle_db = session.execute(
            consulta
        ).scalars().first()

        if detalle_db is None:
            return False

        detalle_db.id_pedido = detalle.id_pedido
        detalle_db.id_producto = detalle.id_producto
        detalle_db.cantidad = detalle.cantidad
        detalle_db.precio_unitario = detalle.precio_unitario
        detalle_db.subtotal = detalle.subtotal

        session.commit()

        return True

    except Exception:
        session.rollback()
        return False

    finally:
        session.close()


def eliminar_detalle_pedido(id_detalle):
    session = SessionLocal()

    try:
        consulta = select(DetallePedido).where(
            DetallePedido.id_detalle == id_detalle
        )

        detalle = session.execute(
            consulta
        ).scalars().first()

        if detalle is None:
            return False

        session.delete(detalle)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False

    finally:
        session.close()