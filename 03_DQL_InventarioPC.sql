SELECT * FROM CATEGORIA;

SELECT * FROM PROVEEDOR;

SELECT * FROM CLIENTE;

SELECT * FROM PRODUCTO;

SELECT * FROM PRODUCTO_PROVEEDOR;

SELECT * FROM PEDIDO;

SELECT * FROM DETALLE_PEDIDO;

SELECT
    id_pedido,
    id_cliente,
    total
FROM PEDIDO;

SELECT * FROM DEVOLUCION;

SELECT * FROM MOVIMIENTO_INVENTARIO;

----------------------------------------------

SELECT nombre, marca, precio_venta
FROM PRODUCTO;

SELECT nombre, descripcion
FROM CATEGORIA;

SELECT nombre, apellido, correo
FROM CLIENTE;

SELECT nombre, marca, modelo 
FROM PRODUCTO 
WHERE nombre = 'Ryzen 5 5600';

SELECT nombre, precio_venta, stock_actual 
FROM PRODUCTO 
WHERE precio_venta > 500 
    AND stock_actual < 10;

SELECT nombre, marca
FROM PRODUCTO
WHERE stock_actual < 5
    OR stock_actual > 20;

SELECT nombre, precio_venta
FROM PRODUCTO
WHERE precio_venta < 500
    OR precio_venta > 1000;

SELECT nombre, precio_venta
FROM PRODUCTO
ORDER BY precio_venta DESC;

SELECT nombre, marca, precio_venta
FROM PRODUCTO
WHERE precio_venta > 500
ORDER BY precio_venta DESC;

SELECT nombre, marca, stock_actual
FROM PRODUCTO
WHERE stock_actual < 10
ORDER BY stock_actual;

SELECT nombre, marca, precio_venta
FROM PRODUCTO
WHERE marca = 'AMD'
    AND precio_venta > 500
ORDER BY precio_venta DESC;

SELECT nombre, marca, stock_actual
FROM PRODUCTO
WHERE (marca = 'AMD' OR marca = 'NVIDIA')
    AND stock_actual < 20
ORDER BY stock_actual;

SELECT nombre, marca, precio_venta
FROM PRODUCTO
WHERE marca IN ('AMD', 'NVIDIA', 'INTEL')
ORDER BY precio_venta DESC;

SELECT nombre, marca, modelo
FROM PRODUCTO
WHERE nombre LIKE '%RTX%';

SELECT nombre, marca, precio_venta
FROM PRODUCTO
WHERE nombre LIKE 'GeForce%';

SELECT nombre, marca, precio_venta, stock_actual
FROM PRODUCTO
WHERE marca IN ('AMD', 'NVIDIA')
    AND precio_venta BETWEEN 500 AND 1500
    AND stock_actual < 20
ORDER BY precio_venta DESC;

SELECT PRODUCTO.nombre, PRODUCTO.marca, CATEGORIA.nombre
FROM PRODUCTO
INNER JOIN CATEGORIA
    ON PRODUCTO.id_categoria = CATEGORIA.id_categoria
WHERE PRODUCTO.marca IN ('AMD');  

SELECT PRODUCTO.nombre, PRODUCTO.marca, CATEGORIA.nombre, PRODUCTO.precio_venta
FROM PRODUCTO
INNER JOIN CATEGORIA
    ON PRODUCTO.id_categoria = CATEGORIA.id_categoria
WHERE PRODUCTO.precio_venta > 500
ORDER BY PRODUCTO.precio_venta DESC;

SELECT PRODUCTO.nombre, PROVEEDOR.nombre, PRODUCTO_PROVEEDOR.costo_proveedor
FROM PRODUCTO
INNER JOIN PRODUCTO_PROVEEDOR
    ON PRODUCTO.id_producto = PRODUCTO_PROVEEDOR.id_producto
INNER JOIN PROVEEDOR
    ON PRODUCTO_PROVEEDOR.id_proveedor = PROVEEDOR.id_proveedor
WHERE PRODUCTO_PROVEEDOR.costo_proveedor > 500
ORDER BY PRODUCTO_PROVEEDOR.costo_proveedor DESC;

SELECT PRODUCTO.nombre, CATEGORIA.nombre, PRODUCTO.precio_venta
FROM PRODUCTO
INNER JOIN CATEGORIA
    ON PRODUCTO.id_categoria = CATEGORIA.id_categoria
WHERE PRODUCTO.precio_venta 
BETWEEN 500 AND 1500
ORDER BY PRODUCTO.precio_venta DESC;

SELECT COUNT(*)
FROM PRODUCTO
WHERE stock_actual < 10;

SELECT AVG(precio_venta)
FROM PRODUCTO;

SELECT MAX(precio_venta)
FROM PRODUCTO;

SELECT MIN(precio_venta)
FROM PRODUCTO;

SELECT marca, COUNT(*)
FROM PRODUCTO
GROUP BY marca;

SELECT marca, AVG(precio_venta)
FROM PRODUCTO
GROUP BY marca;

SELECT marca, COUNT(*)
FROM PRODUCTO
GROUP BY marca
HAVING COUNT(*) > 1;

SELECT marca, SUM(stock_actual)
FROM PRODUCTO
GROUP BY marca
ORDER BY SUM(stock_actual) DESC;

SELECT marca, MAX(precio_venta)
FROM PRODUCTO
GROUP BY marca
ORDER BY MAX(precio_venta) DESC;

SELECT marca, MIN(precio_venta)
FROM PRODUCTO
GROUP BY marca
ORDER BY MIN(precio_venta) ASC;

SELECT CATEGORIA.nombre, COUNT(*)
FROM PRODUCTO
INNER JOIN CATEGORIA
    ON PRODUCTO.id_categoria = CATEGORIA.id_categoria
GROUP BY CATEGORIA.nombre;

SELECT CATEGORIA.nombre, SUM(stock_actual)
FROM PRODUCTO
INNER JOIN CATEGORIA
    ON PRODUCTO.id_categoria = CATEGORIA.id_categoria
WHERE precio_venta > 500
GROUP BY CATEGORIA.nombre;

SELECT CATEGORIA.nombre, SUM(stock_actual)
FROM PRODUCTO
INNER JOIN CATEGORIA
    ON PRODUCTO.id_categoria = CATEGORIA.id_categoria
GROUP BY CATEGORIA.nombre
HAVING SUM(stock_actual) > 20;

SELECT marca, AVG(precio_venta)
FROM PRODUCTO
WHERE precio_venta > 500
GROUP BY marca
HAVING AVG(precio_venta) > 700;

SELECT nombre, marca, precio_venta
FROM PRODUCTO
WHERE precio_venta = (
 SELECT MIN(precio_venta)
 FROM PRODUCTO
 );

SELECT nombre, marca
FROM PRODUCTO
WHERE id_categoria IN (
    SELECT id_categoria
    FROM CATEGORIA
    WHERE nombre LIKE '%Procesadores%'
 );

SELECT marca, COUNT(*)
FROM PRODUCTO
GROUP BY marca
HAVING COUNT(*) > (
    SELECT AVG(cantidad)
    FROM (
        SELECT COUNT(*) AS cantidad
        FROM PRODUCTO
        GROUP BY marca
    ) AS resultados
);

SELECT CATEGORIA.nombre, COUNT(*)
FROM CATEGORIA
INNER JOIN PRODUCTO
ON CATEGORIA.id_categoria = PRODUCTO.id_categoria
GROUP BY CATEGORIA.nombre
HAVING COUNT(*) > (
    SELECT AVG(cantidad)
    FROM (
        SELECT COUNT(*) as cantidad
        FROM PRODUCTO
        GROUP BY PRODUCTO.id_categoria
    ) AS resultados
);


  



