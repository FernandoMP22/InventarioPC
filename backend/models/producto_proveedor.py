from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base


class ProductoProveedor(Base):
    __tablename__ = "PRODUCTO_PROVEEDOR"

    id_producto: Mapped[int] = mapped_column(
        ForeignKey("PRODUCTO.id_producto"),
        primary_key=True
    )

    id_proveedor: Mapped[int] = mapped_column(
        ForeignKey("PROVEEDOR.id_proveedor"),
        primary_key=True
    )

    costo_proveedor: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    codigo_proveedor: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    producto: Mapped["Producto"] = relationship(
        back_populates="proveedores"
    )

    proveedor: Mapped["Proveedor"] = relationship(
        back_populates="productos"
    )