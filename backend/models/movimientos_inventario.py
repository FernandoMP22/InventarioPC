from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base


class MovimientoInventario(Base):
    __tablename__ = "MOVIMIENTO_INVENTARIO"

    id_movimiento: Mapped[int] = mapped_column(
        primary_key=True
    )

    id_producto: Mapped[int] = mapped_column(
        ForeignKey("PRODUCTO.id_producto"),
        nullable=False
    )

    tipo_movimiento: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    cantidad: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    fecha: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    motivo: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    producto: Mapped["Producto"] = relationship()