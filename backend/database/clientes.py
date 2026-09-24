# ==========================================
# CLIENTE
# ==========================================

from database.conexion import obtener_conexion


def obtener_clientes():
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM CLIENTE")

        clientes = cursor.fetchall()

        resultado = []

        for cliente in clientes:
            resultado.append({
                "id_cliente": cliente[0],
                "nombre": cliente[1],
                "apellido": cliente[2],
                "telefono": cliente[3],
                "correo": cliente[4]
            })

        return resultado

    except Exception:
        return None

    finally:
        if cursor:
            cursor.close()

        if conexion:
            conexion.close()


def obtener_cliente(id_cliente):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM CLIENTE WHERE id_cliente = ?",
            (id_cliente,)
        )

        cliente = cursor.fetchone()

        if cliente is None:
            return None

        return {
            "id_cliente": cliente[0],
            "nombre": cliente[1],
            "apellido": cliente[2],
            "telefono": cliente[3],
            "correo": cliente[4]
        }

    except Exception:
        return None

    finally:
        if cursor:
            cursor.close()

        if conexion:
            conexion.close()


def crear_cliente(cliente):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            """
            INSERT INTO CLIENTE
                (nombre, apellido, telefono, correo)
            VALUES (?, ?, ?, ?)
            """,
            (
                cliente.nombre,
                cliente.apellido,
                cliente.telefono,
                cliente.correo
            )
        )

        conexion.commit()

        return True

    except Exception:
        return False

    finally:
        if cursor:
            cursor.close()

        if conexion:
            conexion.close()


def actualizar_cliente(id_cliente, cliente):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            """
            UPDATE CLIENTE
            SET nombre = ?,
                apellido = ?,
                telefono = ?,
                correo = ?
            WHERE id_cliente = ?
            """,
            (
                cliente.nombre,
                cliente.apellido,
                cliente.telefono,
                cliente.correo,
                id_cliente
            )
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    except Exception:
        return False

    finally:
        if cursor:
            cursor.close()

        if conexion:
            conexion.close()


def eliminar_cliente(id_cliente):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM CLIENTE WHERE id_cliente = ?",
            (id_cliente,)
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    except Exception:
        return False

    finally:
        if cursor:
            cursor.close()

        if conexion:
            conexion.close()