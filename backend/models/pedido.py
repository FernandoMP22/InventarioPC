from decimal import Decimal
from datetime import date

from sqlalchemy import Date, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base


class Pedido(Base):
    __tablename__ = "PEDIDO"

    id_pedido: Mapped[int] = mapped_column(
        primary_key=True
    )

    id_cliente: Mapped[int | None] = mapped_column(
        ForeignKey("CLIENTE.id_cliente"),
        nullable=True
    )

    fecha_pedido: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    tipo_envio: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    tipo_entrega: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    estado: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    total: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    cliente: Mapped["Cliente | None"] = relationship(
        back_populates="pedidos"
    )

    detalles: Mapped[list["DetallePedido"]] = relationship(
        back_populates="pedido"
    )