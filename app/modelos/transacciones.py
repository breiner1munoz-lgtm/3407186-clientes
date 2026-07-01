from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modelos.facturas import Factura


class TransaccionesBase(SQLModel):
    cantidad: int
    vr_unitario: float
    descripcion: str
    factura_id: int = Field(foreign_key="factura.id")


class TransaccionesCrear(TransaccionesBase):
    pass


class TransaccionesEditar(TransaccionesBase):
    pass


class Transacciones(TransaccionesBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    factura: Optional["Factura"] = Relationship(back_populates="transacciones")
