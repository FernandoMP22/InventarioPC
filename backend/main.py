from fastapi import FastAPI

from backend.routers import productos
from backend.routers import categorias
from backend.routers import proveedores
from backend.routers import clientes
from backend.routers import productos_proveedores
from backend.routers import pedidos
from backend.routers import detalles_pedido
from backend.routers import movimientos_inventario
from backend.routers import devoluciones


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