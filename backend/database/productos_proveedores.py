from sqlalchemy import select

from backend.models import ProductoProveedor


def obtener_productos_proveedores(session):
    consulta = select(ProductoProveedor)

    resultado = session.execute(consulta)

    return resultado.scalars().all()



def obtener_producto_proveedor(id_producto, id_proveedor, session):
    consulta = select(ProductoProveedor).where(
        ProductoProveedor.id_producto == id_producto,
        ProductoProveedor.id_proveedor == id_proveedor
    )

    resultado = session.execute(consulta)

    return resultado.scalars().first()



def crear_producto_proveedor(producto_proveedor, session):
    try:
        nueva_relacion = ProductoProveedor(
            id_producto=producto_proveedor.id_producto,
            id_proveedor=producto_proveedor.id_proveedor,
            costo_proveedor=producto_proveedor.costo_proveedor,
            codigo_proveedor=producto_proveedor.codigo_proveedor
        )

        session.add(nueva_relacion)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False



def actualizar_producto_proveedor(
    id_producto,
    id_proveedor,
    producto_proveedor,
    session
):
    try:
        consulta = select(ProductoProveedor).where(
            ProductoProveedor.id_producto == id_producto,
            ProductoProveedor.id_proveedor == id_proveedor
        )

        producto_proveedor_db = session.execute(
            consulta
        ).scalars().first()

        if producto_proveedor_db is None:
            return False

        producto_proveedor_db.costo_proveedor = (
            producto_proveedor.costo_proveedor
        )

        producto_proveedor_db.codigo_proveedor = (
            producto_proveedor.codigo_proveedor
        )

        session.commit()

        return True

    except Exception:
        session.rollback()
        return False



def eliminar_producto_proveedor(id_producto, id_proveedor, session):
    try:
        consulta = select(ProductoProveedor).where(
            ProductoProveedor.id_producto == id_producto,
            ProductoProveedor.id_proveedor == id_proveedor
        )

        producto_proveedor = session.execute(
            consulta
        ).scalars().first()

        if producto_proveedor is None:
            return False

        session.delete(producto_proveedor)
        session.commit()

        return True

    except Exception:
        session.rollback()
        return False
