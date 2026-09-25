from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base


class Cliente(Base):
    __tablename__ = "CLIENTE"

    id_cliente: Mapped[int] = mapped_column(
        primary_key=True
    )

    nombre: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    apellido: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    telefono: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    correo: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True
    )

    pedidos: Mapped[list["Pedido"]] = relationship(
        back_populates="cliente"
    )