from contextlib import asynccontextmanager
from pathlib import Path

from sqlmodel import SQLModel, create_engine, Session

BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR / "bd_clientes.sqlite3"
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"
engine = create_engine(DATABASE_URL, echo=True)


@asynccontextmanager
def crear_tablas(app):
    SQLModel.metadata.create_all(engine)
    yield


def get_session():
    with Session(engine) as session:
        yield session
