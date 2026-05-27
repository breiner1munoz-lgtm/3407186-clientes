from datetime import datetime
from fastapi import APIRouter, HTTPException
from app.modelos.facturas import Factura, FacturaCrear, FacturaEditar
from app.modelos.transacciones import Transacciones

router = APIRouter(prefix="/facturas", tags=["facturas"])

# Simulación de base de datos en memoria
lista_facturas: list[Factura] = []
lista_clientes = []  # Referencia compartida desde el enrutador de clientes


@router.get("", response_model=list[Factura])
async def listar_facturas():
    """Obtener todas las facturas"""
    return lista_facturas


@router.get("/{id}", response_model=Factura)
async def obtener_factura(id: int):
    """Obtener una factura por ID"""
    for factura in lista_facturas:
        if factura.id == id:
            return factura
    raise HTTPException(status_code=404, detail="Factura no encontrada")


@router.post("/{cliente_id}", response_model=Factura)
async def crear_factura(cliente_id: int, datos: FacturaCrear):
    """Crear una nueva factura para un cliente"""
    # Nota: En una aplicación real, se buscaría el cliente en la BD
    # Por ahora, validamos que el cliente_id existe en los datos recibidos
    
    factura_nueva = Factura(
        **datos.model_dump(),
        id=len(lista_facturas) + 1
    )
    lista_facturas.append(factura_nueva)
    return factura_nueva


@router.put("/{id}", response_model=Factura)
async def editar_factura(id: int, datos: FacturaEditar):
    """Actualizar una factura existente"""
    for i, factura in enumerate(lista_facturas):
        if factura.id == id:
            factura_actualizada = Factura(
                **datos.model_dump(),
                id=id
            )
            lista_facturas[i] = factura_actualizada
            return factura_actualizada
    raise HTTPException(status_code=404, detail="Factura no encontrada")


@router.delete("/{id}")
async def eliminar_factura(id: int):
    """Eliminar una factura"""
    for i, factura in enumerate(lista_facturas):
        if factura.id == id:
            factura_eliminada = lista_facturas.pop(i)
            return {"mensaje": "Factura eliminada exitosamente", "factura": factura_eliminada}
    raise HTTPException(status_code=404, detail="Factura no encontrada")
