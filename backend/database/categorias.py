# ==========================================
# CATEGORIA
# ==========================================

from database.conexion import obtener_conexion


def obtener_categorias():
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM CATEGORIA")

        categorias = cursor.fetchall()

        resultado = []

        for categoria in categorias:
            resultado.append({
                "id_categoria": categoria[0],
                "nombre": categoria[1],
                "descripcion": categoria[2]
            })

        return resultado

    except Exception:
        return None

    finally:
        if cursor:
            cursor.close()

        if conexion:
            conexion.close()


def obtener_categoria(id_categoria):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM CATEGORIA WHERE id_categoria = ?",
            (id_categoria,)
        )

        categoria = cursor.fetchone()

        if categoria is None:
            return None

        return {
            "id_categoria": categoria[0],
            "nombre": categoria[1],
            "descripcion": categoria[2]
        }

    except Exception:
        return None

    finally:
        if cursor:
            cursor.close()

        if conexion:
            conexion.close()


def crear_categoria(categoria):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            """
            INSERT INTO CATEGORIA (nombre, descripcion)
            VALUES (?, ?)
            """,
            (
                categoria.nombre,
                categoria.descripcion
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


def actualizar_categoria(id_categoria, categoria):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            """
            UPDATE CATEGORIA
            SET nombre = ?,
                descripcion = ?
            WHERE id_categoria = ?
            """,
            (
                categoria.nombre,
                categoria.descripcion,
                id_categoria
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


def eliminar_categoria(id_categoria):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM CATEGORIA WHERE id_categoria = ?",
            (id_categoria,)
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