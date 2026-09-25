# ==========================================
# PRODUCTO
# ==========================================

from backend.database.conexion import obtener_conexion

def obtener_productos():
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM PRODUCTO")

        productos = cursor.fetchall()

        resultado = []

        for producto in productos:
            resultado.append({
                "id_producto": producto[0],
                "nombre": producto[1],
                "marca": producto[2],
                "modelo": producto[3],
                "precio_compra": producto[4],
                "precio_venta": producto[5],
                "stock_actual": producto[6],
                "stock_minimo": producto[7],
                "id_categoria": producto[8]
            })

        return resultado

    except Exception:
        return None

    finally:
        if cursor:
            cursor.close()

        if conexion:
            conexion.close()


def obtener_producto(id_producto):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM PRODUCTO WHERE id_producto = ?",
            (id_producto,)
        )

        producto = cursor.fetchone()

        if producto is None:
            return None

        return {
            "id_producto": producto[0],
            "nombre": producto[1],
            "marca": producto[2],
            "modelo": producto[3],
            "precio_compra": producto[4],
            "precio_venta": producto[5],
            "stock_actual": producto[6],
            "stock_minimo": producto[7],
            "id_categoria": producto[8]
        }

    except Exception:
        return None

    finally:
        if cursor:
            cursor.close()

        if conexion:
            conexion.close()


def crear_producto(producto):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            """
            INSERT INTO PRODUCTO
                (nombre, marca, modelo, precio_compra, precio_venta,
                 stock_actual, stock_minimo, id_categoria)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                producto.nombre,
                producto.marca,
                producto.modelo,
                producto.precio_compra,
                producto.precio_venta,
                producto.stock_actual,
                producto.stock_minimo,
                producto.id_categoria
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


def actualizar_producto(id_producto, producto):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            """
            UPDATE PRODUCTO
            SET nombre = ?,
                marca = ?,
                modelo = ?,
                precio_compra = ?,
                precio_venta = ?,
                stock_actual = ?,
                stock_minimo = ?,
                id_categoria = ?
            WHERE id_producto = ?
            """,
            (
                producto.nombre,
                producto.marca,
                producto.modelo,
                producto.precio_compra,
                producto.precio_venta,
                producto.stock_actual,
                producto.stock_minimo,
                producto.id_categoria,
                id_producto
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


def eliminar_producto(id_producto):
    conexion = None
    cursor = None

    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM PRODUCTO WHERE id_producto = ?",
            (id_producto,)
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