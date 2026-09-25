from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base


class Producto(Base):
    __tablename__ = "PRODUCTO"

    id_producto: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    nombre: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    marca: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    modelo: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True
    )

    precio_compra: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    precio_venta: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    stock_actual: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    stock_minimo: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    id_categoria: Mapped[int | None] = mapped_column(
        ForeignKey("CATEGORIA.id_categoria"),
        nullable=True
    )

    categoria: Mapped["Categoria | None"] = relationship(
        back_populates="productos"
    )

    proveedores: Mapped[list["ProductoProveedor"]] = relationship(
    back_populates="producto"
)