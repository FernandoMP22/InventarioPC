from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base


class Categoria(Base):
    __tablename__ = "CATEGORIA"

    id_categoria: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    nombre: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        unique=True
    )

    descripcion: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    productos: Mapped[list["Producto"]] = relationship(
        back_populates="categoria"
    )