CREATE DATABASE InventarioPC;
USE InventarioPC;

CREATE TABLE CATEGORIA (
    id_categoria INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL UNIQUE,
    descripcion VARCHAR(500)
);

CREATE TABLE PROVEEDOR (
    id_proveedor INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(150) NOT NULL UNIQUE,
    direccion VARCHAR(250)
);

CREATE TABLE CLIENTE (
    id_cliente INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(150)
);

CREATE TABLE PRODUCTO (
    id_producto INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    marca VARCHAR(200) NOT NULL,
    modelo VARCHAR(200),
    precio_compra DECIMAL(10,2),
    precio_venta DECIMAL(10,2),
    stock_actual INT,
    stock_minimo INT,
    id_categoria INT,
    CONSTRAINT FK_PRODUCTO_CATEGORIA
        FOREIGN KEY (id_categoria)
        REFERENCES CATEGORIA(id_categoria)
);

CREATE TABLE PRODUCTO_PROVEEDOR (
    id_producto INT NOT NULL,
    id_proveedor INT NOT NULL,
    costo_proveedor DECIMAL(10,2) NOT NULL,
    codigo_proveedor VARCHAR(50) NOT NULL,

    CONSTRAINT PK_PRODUCTO_PROVEEDOR
        PRIMARY KEY (id_producto, id_proveedor),

    CONSTRAINT FK_PRODUCTO_PROVEEDOR_PRODUCTO
        FOREIGN KEY (id_producto)
        REFERENCES PRODUCTO(id_producto),

    CONSTRAINT FK_PRODUCTO_PROVEEDOR_PROVEEDOR
        FOREIGN KEY (id_proveedor)
        REFERENCES PROVEEDOR(id_proveedor),

    CONSTRAINT UQ_PROVEEDOR_CODIGO
        UNIQUE (id_proveedor, codigo_proveedor)
);

CREATE TABLE PEDIDO (
    id_pedido INT IDENTITY(1,1) PRIMARY KEY,
    id_cliente INT,
    fecha_pedido DATE NOT NULL,
    tipo_envio VARCHAR(100) NOT NULL,
    tipo_entrega VARCHAR(100) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    total DECIMAL(10,2) NOT NULL,

    CONSTRAINT FK_PEDIDO_CLIENTE
        FOREIGN KEY (id_cliente)
        REFERENCES CLIENTE(id_cliente),

    CONSTRAINT CK_PEDIDO_ESTADO
        CHECK (estado IN ('Pendiente', 'En preparación', 'Enviado', 'Entregado', 'Cancelado')),

    CONSTRAINT CK_PEDIDO_TOTAL
        CHECK (total >= 0)
);

CREATE TABLE DETALLE_PEDIDO (
    id_detalle INT IDENTITY(1,1) PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,

    CONSTRAINT FK_DETALLE_PEDIDO_PEDIDO
        FOREIGN KEY (id_pedido)
        REFERENCES PEDIDO(id_pedido),

    CONSTRAINT FK_DETALLE_PEDIDO_PRODUCTO
        FOREIGN KEY (id_producto)
        REFERENCES PRODUCTO(id_producto),

    CONSTRAINT CK_DETALLE_PEDIDO_CANTIDAD
        CHECK (cantidad > 0),

    CONSTRAINT CK_DETALLE_PEDIDO_PRECIO
        CHECK (precio_unitario >= 0),

    CONSTRAINT CK_DETALLE_PEDIDO_SUBTOTAL
        CHECK (subtotal >= 0)
);

CREATE TABLE DEVOLUCION (
    id_devolucion INT IDENTITY(1,1) PRIMARY KEY,
    id_detalle INT NOT NULL,
    fecha_devolucion DATE NOT NULL,
    cantidad INT NOT NULL,
    motivo VARCHAR(200) NOT NULL,
    estado VARCHAR(50) NOT NULL,

    CONSTRAINT FK_DEVOLUCION_DETALLE
        FOREIGN KEY (id_detalle)
        REFERENCES DETALLE_PEDIDO(id_detalle),

    CONSTRAINT CK_DEVOLUCION_CANTIDAD
        CHECK (cantidad > 0),

    CONSTRAINT CK_DEVOLUCION_ESTADO
        CHECK (estado IN ('Pendiente', 'Aprobada', 'Rechazada', 'Procesada'))
);

CREATE TABLE MOVIMIENTO_INVENTARIO (
    id_movimiento INT IDENTITY(1,1) PRIMARY KEY,
    id_producto INT NOT NULL,
    tipo_movimiento VARCHAR(50) NOT NULL,
    cantidad INT NOT NULL,
    fecha DATE NOT NULL,
    motivo VARCHAR(200) NOT NULL,

    CONSTRAINT FK_MOVIMIENTO_PRODUCTO
        FOREIGN KEY (id_producto)
        REFERENCES PRODUCTO(id_producto),

    CONSTRAINT CK_MOVIMIENTO_TIPO
        CHECK (tipo_movimiento IN ('Entrada', 'Salida', 'Devolución', 'Ajuste')),

    CONSTRAINT CK_MOVIMIENTO_CANTIDAD
        CHECK (cantidad > 0)
);

-- Proyecto de gestión de inventario de componentes de PC
-- Cambio realizado en la rama desarrollo
-- Cambio realizado directamente en GitHub
