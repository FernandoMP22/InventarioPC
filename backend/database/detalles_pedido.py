from sqlalchemy import select

from backend.models import DetallePedido


def obtener_detalles_pedido(session):
    consulta = select(DetallePedido)

    resultado = session.execute(consulta)

    return resultado.scalars().all()



def obtener_detalle_pedido(id_detalle, session):
    consulta = select(DetallePedido).where(
        DetallePedido.id_detalle == id_detalle
    )

    resultado = session.execute(consulta)

    return resultado.scalars().first()



def crear_detalle_pedido(detalle, session):
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



def actualizar_detalle_pedido(id_detalle, detalle, session):
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



def eliminar_detalle_pedido(id_detalle, session):
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
