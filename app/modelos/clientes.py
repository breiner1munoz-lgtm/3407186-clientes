from sqlmodel import SQLModel, Field


class ClienteBase(SQLModel):
    nombre: str
    email: str
    descripcion: str | None = None


class ClienteCrear(ClienteBase):
    pass


class ClienteEditar(ClienteBase):
    pass


class Cliente(ClienteBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
