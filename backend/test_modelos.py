from backend.models import (
    Categoria,
    Producto,
    Proveedor,
    Cliente,
    ProductoProveedor,
    Pedido,
    DetallePedido,
    Devolucion,
    MovimientoInventario
)

from backend.models.base import Base


print("Tablas registradas:")

for tabla in Base.metadata.tables:
    print(tabla)