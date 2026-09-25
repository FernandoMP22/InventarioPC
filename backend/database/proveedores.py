# ==========================================
# PROVEEDOR
# ==========================================

from backend.database.conexion import obtener_conexion

def obtener_proveedores():
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM PROVEEDOR")

        proveedores = cursor.fetchall()

        resultado = []

        for proveedor in proveedores:
            resultado.append({
                "id_proveedor": proveedor[0],
                "nombre": proveedor[1],
                "telefono": proveedor[2],
                "correo": proveedor[3],
                "direccion": proveedor[4]
            })

        return resultado

    except Exception:
        return None

    finally:
        if cursor:
            cursor.close()

        if conexion:
            conexion.close()


def obtener_proveedor(id_proveedor):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM PROVEEDOR WHERE id_proveedor = ?",
            (id_proveedor,)
        )

        proveedor = cursor.fetchone()

        if proveedor is None:
            return None

        return {
            "id_proveedor": proveedor[0],
            "nombre": proveedor[1],
            "telefono": proveedor[2],
            "correo": proveedor[3],
            "direccion": proveedor[4]
        }

    except Exception:
        return None

    finally:
        if cursor:
            cursor.close()

        if conexion:
            conexion.close()


def crear_proveedor(proveedor):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            """
            INSERT INTO PROVEEDOR
                (nombre, telefono, correo, direccion)
            VALUES (?, ?, ?, ?)
            """,
            (
                proveedor.nombre,
                proveedor.telefono,
                proveedor.correo,
                proveedor.direccion
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


def actualizar_proveedor(id_proveedor, proveedor):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            """
            UPDATE PROVEEDOR
            SET nombre = ?,
                telefono = ?,
                correo = ?,
                direccion = ?
            WHERE id_proveedor = ?
            """,
            (
                proveedor.nombre,
                proveedor.telefono,
                proveedor.correo,
                proveedor.direccion,
                id_proveedor
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


def eliminar_proveedor(id_proveedor):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM PROVEEDOR WHERE id_proveedor = ?",
            (id_proveedor,)
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