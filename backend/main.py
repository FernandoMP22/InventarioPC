from fastapi import FastAPI

from routers import productos
from routers import categorias
from routers import proveedores
from routers import clientes
from routers import productos_proveedores
from routers import pedidos
from routers import detalles_pedido
from routers import movimientos_inventario
from routers import devoluciones


app = FastAPI()


app.include_router(productos.router)
app.include_router(categorias.router)
app.include_router(proveedores.router)
app.include_router(clientes.router)
app.include_router(productos_proveedores.router)
app.include_router(pedidos.router)
app.include_router(detalles_pedido.router)
app.include_router(movimientos_inventario.router)
app.include_router(devoluciones.router)