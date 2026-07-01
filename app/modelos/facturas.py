from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modelos.clientes import Cliente
    from app.modelos.transacciones import Transacciones


class FacturaBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.now)
    cliente_id: int = Field(foreign_key="cliente.id")
    descripcion: str | None = None


class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente: Optional["Cliente"] = Relationship(back_populates="facturas")
    transacciones: list["Transacciones"] = Relationship(back_populates="factura")
