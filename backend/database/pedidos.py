from datetime import date

from sqlalchemy import select

from backend.models import Pedido


def obtener_pedidos(session):
    consulta = select(Pedido)

    resultado = session.execute(consulta)

    return resultado.scalars().all()



def obtener_pedido(id_pedido, session):
    consulta = select(Pedido).where(
        Pedido.id_pedido == id_pedido
    )

    resultado = session.execute(consulta)

    return resultado.scalars().first()



def crear_pedido(pedido, session):
    try:
        nuevo_pedido = Pedido(
            id_cliente=pedido.id_cliente,
            fecha_pedido=date.fromisoformat(pedido.fecha_pedido),
            tipo_envio=pedido.tipo_envio,
            tipo_entrega=pedido.tipo_entrega,
            estado=pedido.estado,
            total=pedido.total
        )

        session.add(nuevo_pedido)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False



def actualizar_pedido(id_pedido, pedido, session):
    try:
        consulta = select(Pedido).where(
            Pedido.id_pedido == id_pedido
        )

        pedido_db = session.execute(
            consulta
        ).scalars().first()

        if pedido_db is None:
            return False

        pedido_db.id_cliente = pedido.id_cliente
        pedido_db.fecha_pedido = date.fromisoformat(
            pedido.fecha_pedido
        )
        pedido_db.tipo_envio = pedido.tipo_envio
        pedido_db.tipo_entrega = pedido.tipo_entrega
        pedido_db.estado = pedido.estado
        pedido_db.total = pedido.total

        session.commit()

        return True

    except Exception:
        session.rollback()
        return False



def eliminar_pedido(id_pedido, session):
    try:
        consulta = select(Pedido).where(
            Pedido.id_pedido == id_pedido
        )

        pedido = session.execute(
            consulta
        ).scalars().first()

        if pedido is None:
            return False

        session.delete(pedido)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False
