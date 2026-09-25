# ==========================================
# DETALLE_PEDIDO
# ==========================================

from backend.database.conexion import obtener_conexion

def obtener_detalles_pedido():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM DETALLE_PEDIDO")

        detalles = cursor.fetchall()

        detalles_dict = []

        for detalle in detalles:
            detalle_dict = {
                "id_detalle": detalle[0],
                "id_pedido": detalle[1],
                "id_producto": detalle[2],
                "cantidad": detalle[3],
                "precio_unitario": detalle[4],
                "subtotal": detalle[5]
            }

            detalles_dict.append(detalle_dict)

        return detalles_dict

    except Exception as error:
        print("Error al obtener detalles de pedido:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def obtener_detalle_pedido(id_detalle):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "SELECT * FROM DETALLE_PEDIDO WHERE id_detalle = ?",
            (id_detalle,)
        )

        detalle = cursor.fetchone()

        if detalle:
            detalle_dict = {
                "id_detalle": detalle[0],
                "id_pedido": detalle[1],
                "id_producto": detalle[2],
                "cantidad": detalle[3],
                "precio_unitario": detalle[4],
                "subtotal": detalle[5]
            }

            return detalle_dict

        return None

    except Exception as error:
        print("Error al obtener detalle de pedido:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def crear_detalle_pedido(detalle):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO DETALLE_PEDIDO
            (id_pedido, id_producto, cantidad, precio_unitario, subtotal)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                detalle.id_pedido,
                detalle.id_producto,
                detalle.cantidad,
                detalle.precio_unitario,
                detalle.subtotal
            )
        )

        conexion.commit()

        return True

    except Exception as error:
        print("Error al crear detalle de pedido:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def actualizar_detalle_pedido(id_detalle, detalle):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            UPDATE DETALLE_PEDIDO
            SET id_pedido = ?,
                id_producto = ?,
                cantidad = ?,
                precio_unitario = ?,
                subtotal = ?
            WHERE id_detalle = ?
            """,
            (
                detalle.id_pedido,
                detalle.id_producto,
                detalle.cantidad,
                detalle.precio_unitario,
                detalle.subtotal,
                id_detalle
            )
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    except Exception as error:
        print("Error al actualizar detalle de pedido:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def eliminar_detalle_pedido(id_detalle):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "DELETE FROM DETALLE_PEDIDO WHERE id_detalle = ?",
            (id_detalle,)
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    except Exception as error:
        print("Error al eliminar detalle de pedido:", error)
        return False

    finally:
        cursor.close()
        conexion.close()