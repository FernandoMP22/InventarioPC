from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base


class DetallePedido(Base):
    __tablename__ = "DETALLE_PEDIDO"

    id_detalle: Mapped[int] = mapped_column(
        primary_key=True
    )

    id_pedido: Mapped[int] = mapped_column(
        ForeignKey("PEDIDO.id_pedido"),
        nullable=False
    )

    id_producto: Mapped[int] = mapped_column(
        ForeignKey("PRODUCTO.id_producto"),
        nullable=False
    )

    cantidad: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    precio_unitario: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    subtotal: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    pedido: Mapped["Pedido"] = relationship(
        back_populates="detalles"
    )

    producto: Mapped["Producto"] = relationship()
    
    devoluciones: Mapped[list["Devolucion"]] = relationship(
        back_populates="detalle"
    )