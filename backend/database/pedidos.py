# ==========================================
# PEDIDO
# ==========================================

from backend.database.conexion import obtener_conexion

def obtener_pedidos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM PEDIDO")

        pedidos = cursor.fetchall()

        pedidos_dict = []

        for pedido in pedidos:
            pedido_dict = {
                "id_pedido": pedido[0],
                "id_cliente": pedido[1],
                "fecha_pedido": pedido[2],
                "tipo_envio": pedido[3],
                "tipo_entrega": pedido[4],
                "estado": pedido[5],
                "total": pedido[6]
            }

            pedidos_dict.append(pedido_dict)

        return pedidos_dict

    except Exception as error:
        print("Error al obtener pedidos:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def obtener_pedido(id_pedido):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "SELECT * FROM PEDIDO WHERE id_pedido = ?",
            (id_pedido,)
        )

        pedido = cursor.fetchone()

        if pedido:
            pedido_dict = {
                "id_pedido": pedido[0],
                "id_cliente": pedido[1],
                "fecha_pedido": pedido[2],
                "tipo_envio": pedido[3],
                "tipo_entrega": pedido[4],
                "estado": pedido[5],
                "total": pedido[6]
            }

            return pedido_dict

        return None

    except Exception as error:
        print("Error al obtener pedido:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def crear_pedido(pedido):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO PEDIDO
            (id_cliente, fecha_pedido, tipo_envio, tipo_entrega, estado, total)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                pedido.id_cliente,
                pedido.fecha_pedido,
                pedido.tipo_envio,
                pedido.tipo_entrega,
                pedido.estado,
                pedido.total
            )
        )

        conexion.commit()

        return True

    except Exception as error:
        print("Error al crear pedido:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def actualizar_pedido(id_pedido, pedido):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            UPDATE PEDIDO
            SET id_cliente = ?,
                fecha_pedido = ?,
                tipo_envio = ?,
                tipo_entrega = ?,
                estado = ?,
                total = ?
            WHERE id_pedido = ?
            """,
            (
                pedido.id_cliente,
                pedido.fecha_pedido,
                pedido.tipo_envio,
                pedido.tipo_entrega,
                pedido.estado,
                pedido.total,
                id_pedido
            )
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    except Exception as error:
        print("Error al actualizar pedido:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def eliminar_pedido(id_pedido):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "DELETE FROM PEDIDO WHERE id_pedido = ?",
            (id_pedido,)
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    except Exception as error:
        print("Error al eliminar pedido:", error)
        return False

    finally:
        cursor.close()
        conexion.close()