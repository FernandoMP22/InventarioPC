# ==========================================
# DEVOLUCION
# ==========================================

from database.conexion import obtener_conexion


def obtener_devoluciones():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM DEVOLUCION")

        devoluciones = cursor.fetchall()

        devoluciones_dict = []

        for devolucion in devoluciones:
            devolucion_dict = {
                "id_devolucion": devolucion[0],
                "id_detalle": devolucion[1],
                "fecha_devolucion": devolucion[2],
                "cantidad": devolucion[3],
                "motivo": devolucion[4],
                "estado": devolucion[5]
            }

            devoluciones_dict.append(devolucion_dict)

        return devoluciones_dict

    except Exception as error:
        print("Error al obtener devoluciones:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def obtener_devolucion(id_devolucion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "SELECT * FROM DEVOLUCION WHERE id_devolucion = ?",
            (id_devolucion,)
        )

        devolucion = cursor.fetchone()

        if devolucion:
            devolucion_dict = {
                "id_devolucion": devolucion[0],
                "id_detalle": devolucion[1],
                "fecha_devolucion": devolucion[2],
                "cantidad": devolucion[3],
                "motivo": devolucion[4],
                "estado": devolucion[5]
            }

            return devolucion_dict

        return None

    except Exception as error:
        print("Error al obtener devolucion:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def crear_devolucion(devolucion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO DEVOLUCION
            (id_detalle, fecha_devolucion, cantidad, motivo, estado)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                devolucion.id_detalle,
                devolucion.fecha_devolucion,
                devolucion.cantidad,
                devolucion.motivo,
                devolucion.estado
            )
        )

        conexion.commit()

        return True

    except Exception as error:
        print("Error al crear devolucion:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def actualizar_devolucion(id_devolucion, devolucion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            UPDATE DEVOLUCION
            SET id_detalle = ?,
                fecha_devolucion = ?,
                cantidad = ?,
                motivo = ?,
                estado = ?
            WHERE id_devolucion = ?
            """,
            (
                devolucion.id_detalle,
                devolucion.fecha_devolucion,
                devolucion.cantidad,
                devolucion.motivo,
                devolucion.estado,
                id_devolucion
            )
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    except Exception as error:
        print("Error al actualizar devolucion:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def eliminar_devolucion(id_devolucion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "DELETE FROM DEVOLUCION WHERE id_devolucion = ?",
            (id_devolucion,)
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    except Exception as error:
        print("Error al eliminar devolucion:", error)
        return False

    finally:
        cursor.close()
        conexion.close()