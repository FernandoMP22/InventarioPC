# ==========================================
# MOVIMIENTO_INVENTARIO
# ==========================================

from database.conexion import obtener_conexion


def obtener_movimientos_inventario():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM MOVIMIENTO_INVENTARIO")

        movimientos = cursor.fetchall()

        movimientos_dict = []

        for movimiento in movimientos:
            movimiento_dict = {
                "id_movimiento": movimiento[0],
                "id_producto": movimiento[1],
                "tipo_movimiento": movimiento[2],
                "cantidad": movimiento[3],
                "fecha": movimiento[4],
                "motivo": movimiento[5]
            }

            movimientos_dict.append(movimiento_dict)

        return movimientos_dict

    except Exception as error:
        print("Error al obtener movimientos de inventario:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def obtener_movimiento_inventario(id_movimiento):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            SELECT * FROM MOVIMIENTO_INVENTARIO
            WHERE id_movimiento = ?
            """,
            (id_movimiento,)
        )

        movimiento = cursor.fetchone()

        if movimiento:
            movimiento_dict = {
                "id_movimiento": movimiento[0],
                "id_producto": movimiento[1],
                "tipo_movimiento": movimiento[2],
                "cantidad": movimiento[3],
                "fecha": movimiento[4],
                "motivo": movimiento[5]
            }

            return movimiento_dict

        return None

    except Exception as error:
        print("Error al obtener movimiento de inventario:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def crear_movimiento_inventario(movimiento):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO MOVIMIENTO_INVENTARIO
            (id_producto, tipo_movimiento, cantidad, fecha, motivo)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                movimiento.id_producto,
                movimiento.tipo_movimiento,
                movimiento.cantidad,
                movimiento.fecha,
                movimiento.motivo
            )
        )

        conexion.commit()

        return True

    except Exception as error:
        print("Error al crear movimiento de inventario:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def actualizar_movimiento_inventario(id_movimiento, movimiento):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            UPDATE MOVIMIENTO_INVENTARIO
            SET id_producto = ?,
                tipo_movimiento = ?,
                cantidad = ?,
                fecha = ?,
                motivo = ?
            WHERE id_movimiento = ?
            """,
            (
                movimiento.id_producto,
                movimiento.tipo_movimiento,
                movimiento.cantidad,
                movimiento.fecha,
                movimiento.motivo,
                id_movimiento
            )
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    except Exception as error:
        print("Error al actualizar movimiento de inventario:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def eliminar_movimiento_inventario(id_movimiento):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            DELETE FROM MOVIMIENTO_INVENTARIO
            WHERE id_movimiento = ?
            """,
            (id_movimiento,)
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    except Exception as error:
        print("Error al eliminar movimiento de inventario:", error)
        return False

    finally:
        cursor.close()
        conexion.close()