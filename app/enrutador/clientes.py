from fastapi import APIRouter, HTTPException
from app.modelos.clientes import Cliente, ClienteCrear, ClienteEditar

router = APIRouter(prefix="/clientes", tags=["clientes"])

# Simulación de base de datos en memoria
lista_clientes: list[Cliente] = []


@router.get("")
async def listar_clientes():
    """Obtener todos los clientes"""
    return {"clientes": lista_clientes, "total": len(lista_clientes)}


@router.get("/{id}")
async def obtener_cliente(id: int):
    """Obtener un cliente por ID"""
    for cliente in lista_clientes:
        if cliente.id == id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@router.post("", response_model=Cliente)
async def crear_cliente(datos: ClienteCrear):
    """Crear un nuevo cliente"""
    nuevo_cliente = Cliente(
        **datos.model_dump(),
        id=len(lista_clientes) + 1
    )
    lista_clientes.append(nuevo_cliente)
    return nuevo_cliente


@router.put("/{id}", response_model=Cliente)
async def editar_cliente(id: int, datos: ClienteEditar):
    """Actualizar un cliente existente"""
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            cliente_actualizado = Cliente(
                **datos.model_dump(),
                id=id
            )
            lista_clientes[i] = cliente_actualizado
            return cliente_actualizado
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


@router.delete("/{id}")
async def eliminar_cliente(id: int):
    """Eliminar un cliente"""
    for i, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            cliente_eliminado = lista_clientes.pop(i)
            return {"mensaje": "Cliente eliminado exitosamente", "cliente": cliente_eliminado}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")
