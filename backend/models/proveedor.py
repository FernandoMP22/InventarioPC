from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base


class Proveedor(Base):
    __tablename__ = "PROVEEDOR"

    id_proveedor: Mapped[int] = mapped_column(
        primary_key=True
    )

    nombre: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    telefono: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    correo: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        unique=True
    )

    direccion: Mapped[str | None] = mapped_column(
        String(250),
        nullable=True
    )

    productos: Mapped[list["ProductoProveedor"]] = relationship(
        back_populates="proveedor"
    )