import pyodbc

def obtener_conexion():
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=DESKTOP-VTAJONH\\SQLEXPRESS;"
        "DATABASE=InventarioPC;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    return conexion

# ==========================================
# PRODUCTO
# ==========================================


def obtener_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM PRODUCTO")
        productos = cursor.fetchall()

        productos_dict = []

        for producto in productos:
            producto_dict = {
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

            productos_dict.append(producto_dict)

        return productos_dict

    except Exception as error:
        print("Error al obtener productos:", error)
        return False

    finally:
        cursor.close()
        conexion.close()

def obtener_producto(id_producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "SELECT * FROM PRODUCTO WHERE id_producto = ?",
            (id_producto,)
        )

        producto = cursor.fetchone()

        if producto:
            producto_dict = {
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

            return producto_dict

        return None

    except Exception as error:
        print("Error al obtener producto:", error)
        return False

    finally:
        cursor.close()
        conexion.close()

def crear_producto(producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO PRODUCTO
            (nombre, marca, modelo, precio_compra, precio_venta, stock_actual, stock_minimo, id_categoria)
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

    except Exception as error:
        print("Error al crear producto:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def actualizar_producto(id_producto, producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
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

    except Exception as error:
        print("Error al actualizar producto:", error)
        return False

    finally:
        cursor.close()
        conexion.close()

def eliminar_producto(id_producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "DELETE FROM PRODUCTO WHERE id_producto = ?",
            (id_producto,)
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()
        return True

    except Exception as error:
        print("Error al eliminar producto:", error)
        return False

    finally:
        cursor.close()
        conexion.close()

# ==========================================
# CATEGORIA
# ==========================================

def obtener_categorias():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM CATEGORIA")
        categorias = cursor.fetchall()

        categorias_dict = []

        for categoria in categorias:
            categoria_dict = {
                "id_categoria": categoria[0],
                "nombre": categoria[1],
                "descripcion": categoria[2]
            }

            categorias_dict.append(categoria_dict)

        return categorias_dict

    except Exception as error:
        print("Error al obtener categorias:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def obtener_categoria(id_categoria):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "SELECT * FROM CATEGORIA WHERE id_categoria = ?",
            (id_categoria,)
        )

        categoria = cursor.fetchone()

        if categoria:
            categoria_dict = {
                "id_categoria": categoria[0],
                "nombre": categoria[1],
                "descripcion": categoria[2]
            }

            return categoria_dict

        return None

    except Exception as error:
        print("Error al obtener categoria:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def crear_categoria(categoria):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO CATEGORIA
            (nombre, descripcion)
            VALUES (?, ?)
            """,
            (
                categoria.nombre,
                categoria.descripcion
            )
        )

        conexion.commit()
        return True

    except Exception as error:
        print("Error al crear categoria:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def actualizar_categoria(id_categoria, categoria):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
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

    except Exception as error:
        print("Error al actualizar categoria:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def eliminar_categoria(id_categoria):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "DELETE FROM CATEGORIA WHERE id_categoria = ?",
            (id_categoria,)
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()
        return True

    except Exception as error:
        print("Error al eliminar categoria:", error)
        return False

    finally:
        cursor.close()
        conexion.close()

# ==========================================
# PROVEEDOR
# ==========================================

def obtener_proveedores():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM PROVEEDOR")
        proveedores = cursor.fetchall()

        proveedores_dict = []

        for proveedor in proveedores:
            proveedor_dict = {
                "id_proveedor": proveedor[0],
                "nombre": proveedor[1],
                "telefono": proveedor[2],
                "correo": proveedor[3],
                "direccion": proveedor[4]
            }

            proveedores_dict.append(proveedor_dict)

        return proveedores_dict

    except Exception as error:
        print("Error al obtener proveedores:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def obtener_proveedor(id_proveedor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "SELECT * FROM PROVEEDOR WHERE id_proveedor = ?",
            (id_proveedor,)
        )

        proveedor = cursor.fetchone()

        if proveedor:
            proveedor_dict = {
                "id_proveedor": proveedor[0],
                "nombre": proveedor[1],
                "telefono": proveedor[2],
                "correo": proveedor[3],
                "direccion": proveedor[4]
            }

            return proveedor_dict

        return None

    except Exception as error:
        print("Error al obtener proveedor:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def crear_proveedor(proveedor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
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

    except Exception as error:
        print("Error al crear proveedor:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def actualizar_proveedor(id_proveedor, proveedor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
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

    except Exception as error:
        print("Error al actualizar proveedor:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def eliminar_proveedor(id_proveedor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "DELETE FROM PROVEEDOR WHERE id_proveedor = ?",
            (id_proveedor,)
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()
        return True

    except Exception as error:
        print("Error al eliminar proveedor:", error)
        return False

    finally:
        cursor.close()
        conexion.close()

# ==========================================
# CLIENTE
# ==========================================

def obtener_clientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM CLIENTE")

        clientes = cursor.fetchall()

        clientes_dict = []

        for cliente in clientes:
            cliente_dict = {
                "id_cliente": cliente[0],
                "nombre": cliente[1],
                "apellido": cliente[2],
                "telefono": cliente[3],
                "correo": cliente[4]
            }

            clientes_dict.append(cliente_dict)

        return clientes_dict

    except Exception as error:
        print("Error al obtener clientes:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def obtener_cliente(id_cliente):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "SELECT * FROM CLIENTE WHERE id_cliente = ?",
            (id_cliente,)
        )

        cliente = cursor.fetchone()

        if cliente:
            cliente_dict = {
                "id_cliente": cliente[0],
                "nombre": cliente[1],
                "apellido": cliente[2],
                "telefono": cliente[3],
                "correo": cliente[4]
            }

            return cliente_dict

        return None

    except Exception as error:
        print("Error al obtener cliente:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def crear_cliente(cliente):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
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

    except Exception as error:
        print("Error al crear cliente:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def actualizar_cliente(id_cliente, cliente):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
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

    except Exception as error:
        print("Error al actualizar cliente:", error)
        return False

    finally:
        cursor.close()
        conexion.close()


def eliminar_cliente(id_cliente):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "DELETE FROM CLIENTE WHERE id_cliente = ?",
            (id_cliente,)
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    except Exception as error:
        print("Error al eliminar cliente:", error)
        return False

    finally:
        cursor.close()
        conexion.close()

# ==========================================
# PRODUCTO_PROVEEDOR
# ==========================================

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


def actualizar_producto_proveedor(
    id_producto,
    id_proveedor,
    producto_proveedor
):
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

# ==========================================
# PEDIDO
# ==========================================

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

# ==========================================
# DETALLE_PEDIDO
# ==========================================

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

# ==========================================
# MOVIMIENTO_INVENTARIO
# ==========================================

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

# ==========================================
# DEVOLUCION
# ==========================================

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