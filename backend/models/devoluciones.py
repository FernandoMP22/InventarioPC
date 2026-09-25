from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base


class Devolucion(Base):
    __tablename__ = "DEVOLUCION"

    id_devolucion: Mapped[int] = mapped_column(
        primary_key=True
    )

    id_detalle: Mapped[int] = mapped_column(
        ForeignKey("DETALLE_PEDIDO.id_detalle"),
        nullable=False
    )

    fecha_devolucion: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    cantidad: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    motivo: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    estado: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    detalle: Mapped["DetallePedido"] = relationship(
        back_populates="devoluciones"
    )