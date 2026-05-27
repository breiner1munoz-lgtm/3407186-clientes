from fastapi import FastAPI
from app.enrutador.clientes import router as clientes_router
from app.enrutador.facturas import router as facturas_router
from app.enrutador.transacciones import router as transacciones_router

app = FastAPI(
    title="API Gestión de Clientes",
    description="API para gestionar clientes, facturas y transacciones",
    version="1.0.0"
)

# Incluir enrutadores
app.include_router(clientes_router)
app.include_router(facturas_router)
app.include_router(transacciones_router)


@app.get("/")
async def root():
    """Endpoint raíz - Bienvenida"""
    return {
        "mensaje": "Bienvenido a la API de Gestión de Clientes",
        "versión": "1.0.0",
        "documentación": "/docs"
    }


@app.get("/health")
async def health_check():
    """Verificar que la API está funcionando"""
    return {"estado": "La API está funcionando correctamente"}
