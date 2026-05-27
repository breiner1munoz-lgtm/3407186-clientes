from fastapi import APIRouter, HTTPException
from app.modelos.transacciones import Transacciones, TransaccionesCrear, TransaccionesEditar

router = APIRouter(prefix="/transacciones", tags=["transacciones"])

# Simulación de base de datos en memoria
lista_transacciones: list[Transacciones] = []


@router.get("")
async def listar_transacciones():
    """Obtener todas las transacciones"""
    return {"transacciones": lista_transacciones, "total": len(lista_transacciones)}


@router.get("/{id}")
async def obtener_transaccion(id: int):
    """Obtener una transacción por ID"""
    for transaccion in lista_transacciones:
        if transaccion.id == id:
            return transaccion
    raise HTTPException(status_code=404, detail="Transacción no encontrada")


@router.post("", response_model=Transacciones)
async def crear_transaccion(datos: TransaccionesCrear):
    """Crear una nueva transacción"""
    nueva_transaccion = Transacciones(
        **datos.model_dump(),
        id=len(lista_transacciones) + 1
    )
    lista_transacciones.append(nueva_transaccion)
    return nueva_transaccion


@router.put("/{id}", response_model=Transacciones)
async def editar_transaccion(id: int, datos: TransaccionesEditar):
    """Actualizar una transacción existente"""
    for i, transaccion in enumerate(lista_transacciones):
        if transaccion.id == id:
            transaccion_actualizada = Transacciones(
                **datos.model_dump(),
                id=id,
                factura_id=transaccion.factura_id
            )
            lista_transacciones[i] = transaccion_actualizada
            return transaccion_actualizada
    raise HTTPException(status_code=404, detail="Transacción no encontrada")


@router.delete("/{id}")
async def eliminar_transaccion(id: int):
    """Eliminar una transacción"""
    for i, transaccion in enumerate(lista_transacciones):
        if transaccion.id == id:
            transaccion_eliminada = lista_transacciones.pop(i)
            return {"mensaje": "Transacción eliminada", "transaccion": transaccion_eliminada}
    raise HTTPException(status_code=404, detail="Transacción no encontrada")


@router.get("/factura/{factura_id}")
async def obtener_transacciones_por_factura(factura_id: int):
    """Obtener todas las transacciones de una factura"""
    transacciones_factura = [
        t for t in lista_transacciones
        if t.factura_id == factura_id
    ]
    if not transacciones_factura:
        raise HTTPException(status_code=404, detail="No hay transacciones para esta factura")
    return {"transacciones": transacciones_factura, "total": len(transacciones_factura)}
