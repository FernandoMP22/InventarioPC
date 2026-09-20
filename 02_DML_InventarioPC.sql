INSERT INTO CATEGORIA (nombre, descripcion)
VALUES
('Procesadores', 'Componentes encargados de ejecutar las instrucciones del sistema.'),
('Tarjetas gráficas', 'Componentes utilizados para procesamiento y renderizado gráfico.'),
('Memoria RAM', 'Memoria temporal utilizada por el sistema para ejecutar programas.'),
('Almacenamiento', 'Dispositivos utilizados para almacenar información y archivos.');

INSERT INTO PROVEEDOR (nombre, telefono, correo, direccion)
VALUES
('Tech Distribuciones', '5555-1001', 'ventas@techdistribuciones.com', 'Ciudad de Guatemala'),
('PC Supply Guatemala', '5555-1002', 'contacto@pcsupply.com', 'Zona 10, Guatemala'),
('Componentes GT', '5555-1003', 'ventas@componentesgt.com', 'Zona 12, Guatemala');

INSERT INTO CLIENTE (nombre, apellido, telefono, correo)
VALUES
('Carlos', 'López', '5555-2001', 'carlos.lopez@gmail.com'),
('María', 'García', '5555-2002', 'maria.garcia@gmail.com'),
('Daniel', 'Méndez', '5555-2003', 'daniel.mendez@gmail.com'),
('Andrea', 'Ramírez', '5555-2004', 'andrea.ramirez@gmail.com');

INSERT INTO PRODUCTO
    (nombre, marca, modelo, precio_compra, precio_venta, stock_actual, stock_minimo, id_categoria)
VALUES
    ('Ryzen 5 5600', 'AMD', '5600', 650.00, 899.00, 8, 3, 1),
    ('GeForce RTX 4060', 'NVIDIA', 'RTX 4060', 2200.00, 2799.00, 5, 2, 2),
    ('Fury Beast 16GB', 'Kingston', 'KF432C16BB/16', 350.00, 499.00, 12, 4, 3),
    ('NV3 1TB', 'Kingston', 'SNV3S/1000G', 450.00, 599.00, 10, 3, 4),
    ('Core i5-14400F', 'Intel', 'i5-14400F', 1200.00, 1599.00, 6, 2, 1);

INSERT INTO PRODUCTO_PROVEEDOR
    (id_producto, id_proveedor, costo_proveedor, codigo_proveedor)
VALUES
    (1, 1, 650.00, 'AMD-R5600'),
    (1, 2, 625.00, 'RYZ-5600'),
    (2, 1, 2200.00, 'NV-4060'),
    (2, 3, 2150.00, 'RTX4060-GT'),
    (3, 1, 350.00, 'KNG-RAM16'),
    (4, 2, 450.00, 'KNG-NV3-1T'),
    (4, 3, 440.00, 'NV3-1TB-GT'),
    (5, 2, 1200.00, 'INT-I5144');

INSERT INTO PEDIDO
    (id_cliente, fecha_pedido, tipo_envio, tipo_entrega, estado, total)
VALUES
    (1, '2026-09-15', 'Mensajería', 'Domicilio', 'Pendiente', 0.00),
    (2, '2026-09-15', 'Empresa de transporte', 'Punto de entrega', 'Pendiente', 0.00),
    (3, '2026-09-15', 'Ninguno', 'Recoger en tienda', 'En preparación', 0.00),
    (4, '2026-09-15', 'Mensajería', 'Domicilio', 'Pendiente', 0.00);

INSERT INTO DETALLE_PEDIDO
    (id_pedido, id_producto, cantidad, precio_unitario, subtotal)
VALUES
    (1, 1, 1, 899.00, 899.00),
    (1, 3, 2, 499.00, 998.00),
    (2, 2, 1, 2799.00, 2799.00),
    (2, 4, 1, 599.00, 599.00),
    (3, 5, 1, 1599.00, 1599.00),
    (3, 3, 1, 499.00, 499.00),
    (4, 1, 2, 899.00, 1798.00);

UPDATE p
SET total = (
    SELECT COALESCE(SUM(d.subtotal), 0)
    FROM DETALLE_PEDIDO AS d
    WHERE d.id_pedido = p.id_pedido
)
FROM PEDIDO AS p;

INSERT INTO DEVOLUCION
    (id_detalle, fecha_devolucion, cantidad, motivo, estado)
VALUES
    (2, '2026-09-15', 1, 'Producto con falla', 'Pendiente'),
    (4, '2026-09-15', 1, 'Producto incorrecto', 'Aprobada'),
    (6, '2026-09-15', 1, 'Cambio de producto', 'Procesada');

INSERT INTO MOVIMIENTO_INVENTARIO
    (id_producto, tipo_movimiento, cantidad, fecha, motivo)
VALUES
    (1, 'Entrada', 5, '2026-09-15', 'Ingreso de mercadería'),
    (2, 'Entrada', 3, '2026-09-15', 'Ingreso de mercadería'),
    (3, 'Salida', 2, '2026-09-15', 'Venta de producto'),
    (4, 'Salida', 1, '2026-09-15', 'Venta de producto'),
    (5, 'Salida', 1, '2026-09-15', 'Venta de producto'),
    (3, 'Devolución', 1, '2026-09-15', 'Devolución de cliente'),
    (4, 'Ajuste', 1, '2026-09-15', 'Ajuste por revisión de inventario');