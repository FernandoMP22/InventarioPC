from sqlalchemy import select

from backend.database.session import SessionLocal
from backend.models import Cliente


def obtener_clientes():
    session = SessionLocal()

    try:
        consulta = select(Cliente)

        resultado = session.execute(consulta)

        return resultado.scalars().all()

    finally:
        session.close()


def obtener_cliente(id_cliente):
    session = SessionLocal()

    try:
        consulta = select(Cliente).where(
            Cliente.id_cliente == id_cliente
        )

        resultado = session.execute(consulta)

        return resultado.scalars().first()

    finally:
        session.close()


def crear_cliente(cliente):
    session = SessionLocal()

    try:
        nuevo_cliente = Cliente(
            nombre=cliente.nombre,
            apellido=cliente.apellido,
            telefono=cliente.telefono,
            correo=cliente.correo
        )

        session.add(nuevo_cliente)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False

    finally:
        session.close()


def actualizar_cliente(id_cliente, cliente):
    session = SessionLocal()

    try:
        consulta = select(Cliente).where(
            Cliente.id_cliente == id_cliente
        )

        cliente_db = session.execute(
            consulta
        ).scalars().first()

        if cliente_db is None:
            return False

        cliente_db.nombre = cliente.nombre
        cliente_db.apellido = cliente.apellido
        cliente_db.telefono = cliente.telefono
        cliente_db.correo = cliente.correo

        session.commit()

        return True

    except Exception:
        session.rollback()
        return False

    finally:
        session.close()


def eliminar_cliente(id_cliente):
    session = SessionLocal()

    try:
        consulta = select(Cliente).where(
            Cliente.id_cliente == id_cliente
        )

        cliente = session.execute(
            consulta
        ).scalars().first()

        if cliente is None:
            return False

        session.delete(cliente)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False

    finally:
        session.close()