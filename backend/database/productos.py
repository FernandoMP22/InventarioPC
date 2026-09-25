from sqlalchemy import select

from backend.models import Producto


def obtener_productos(session):
    consulta = select(Producto)

    resultado = session.execute(consulta)

    productos = resultado.scalars().all()

    return productos


def obtener_producto(id_producto, session):
    consulta = select(Producto).where(
        Producto.id_producto == id_producto
    )

    resultado = session.execute(consulta)

    producto = resultado.scalars().first()

    return producto


def crear_producto(producto, session):
    try:
        nuevo_producto = Producto(
            nombre=producto.nombre,
            marca=producto.marca,
            modelo=producto.modelo,
            precio_compra=producto.precio_compra,
            precio_venta=producto.precio_venta,
            stock_actual=producto.stock_actual,
            stock_minimo=producto.stock_minimo,
            id_categoria=producto.id_categoria
        )

        session.add(nuevo_producto)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False


def actualizar_producto(id_producto, producto, session):
    try:
        consulta = select(Producto).where(
            Producto.id_producto == id_producto
        )

        producto_db = session.execute(consulta).scalars().first()

        if producto_db is None:
            return False

        producto_db.nombre = producto.nombre
        producto_db.marca = producto.marca
        producto_db.modelo = producto.modelo
        producto_db.precio_compra = producto.precio_compra
        producto_db.precio_venta = producto.precio_venta
        producto_db.stock_actual = producto.stock_actual
        producto_db.stock_minimo = producto.stock_minimo
        producto_db.id_categoria = producto.id_categoria

        session.commit()

        return True

    except Exception:
        session.rollback()
        return False


def eliminar_producto(id_producto, session):
    try:
        consulta = select(Producto).where(
            Producto.id_producto == id_producto
        )

        producto = session.execute(consulta).scalars().first()

        if producto is None:
            return False

        session.delete(producto)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False
