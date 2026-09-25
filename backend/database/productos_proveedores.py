# ==========================================
# PRODUCTO_PROVEEDOR
# ==========================================

from backend.database.conexion import obtener_conexion

def obtener_productos_proveedores():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM PRODUCTO_PROVEEDOR")

        productos_proveedores = cursor.fetchall()

        productos_proveedores_dict = []

        for producto_proveedor in productos_proveedores:
            producto_proveedor_dict = {
                "id_producto": producto_proveedor[0],
                "id_proveedor": producto_proveedor[1],
                "costo_proveedor": producto_proveedor[2],
                "codigo_proveedor": producto_proveedor[3]
            }

            productos_proveedores_dict.append(producto_proveedor_dict)

        return productos_proveedores_dict

    except Exception as error:
        print("Error al obtener relaciones producto-proveedor:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def obtener_producto_proveedor(id_producto, id_proveedor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            SELECT * FROM PRODUCTO_PROVEEDOR
            WHERE id_producto = ? AND id_proveedor = ?
            """,
            (id_producto, id_proveedor)
        )

        producto_proveedor = cursor.fetchone()

        if producto_proveedor:
            producto_proveedor_dict = {
                "id_producto": producto_proveedor[0],
                "id_proveedor": producto_proveedor[1],
                "costo_proveedor": producto_proveedor[2],
                "codigo_proveedor": producto_proveedor[3]
            }

            return producto_proveedor_dict

        return None

    except Exception as error:
        print("Error al obtener relación producto-proveedor:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def crear_producto_proveedor(producto_proveedor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO PRODUCTO_PROVEEDOR
            (id_producto, id_proveedor, costo_proveedor, codigo_proveedor)
            VALUES (?, ?, ?, ?)
            """,
            (
                producto_proveedor.id_producto,
                producto_proveedor.id_proveedor,
                producto_proveedor.costo_proveedor,
                producto_proveedor.codigo_proveedor
            )
        )

        conexion.commit()

        return True

    except Exception as error:
        print("Error al crear relación producto-proveedor:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def actualizar_producto_proveedor(id_producto, id_proveedor, producto_proveedor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            UPDATE PRODUCTO_PROVEEDOR
            SET costo_proveedor = ?,
                codigo_proveedor = ?
            WHERE id_producto = ? AND id_proveedor = ?
            """,
            (
                producto_proveedor.costo_proveedor,
                producto_proveedor.codigo_proveedor,
                id_producto,
                id_proveedor
            )
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    except Exception as error:
        print("Error al actualizar relación producto-proveedor:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def eliminar_producto_proveedor(id_producto, id_proveedor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            DELETE FROM PRODUCTO_PROVEEDOR
            WHERE id_producto = ? AND id_proveedor = ?
            """,
            (id_producto, id_proveedor)
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    except Exception as error:
        print("Error al eliminar relación producto-proveedor:", error)
        return False

    finally:
        cursor.close()
        conexion.close()