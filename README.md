# API Gestión de Clientes

Proyecto educativo para gestionar clientes, facturas y transacciones con FastAPI.

## Autor
**Nombre:** Breiner Stanly Muñoz Martinez
**Email:** Breiner1munoz@gmail.com  
**Ficha:** 3407186

---

## ¿Qué hace este proyecto?

- Crear, leer, actualizar y eliminar clientes (CRUD)
- Gestionar facturas de clientes
- Registrar transacciones de productos/servicios

---

## Pasos para ejecutar

### 1. Instalar Python
Descargar de: https://www.python.org/

### 2. Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la API
```bash
uvicorn app.main:app --reload
```

Abre: http://127.0.0.1:8000/docs

---

## Carpetas del proyecto

```
app/
├── main.py              → API principal
├── modelos/             → Estructura de datos (Clientes, Facturas, Transacciones)
└── enrutador/           → Rutas/Endpoints (Clientes, Facturas, Transacciones)
```

---

## Endpoints principales

**Clientes:** `/clientes`  
**Facturas:** `/facturas`  
**Transacciones:** `/transacciones`

---

## Tareas realizadas

1. Creada estructura profesional de carpetas
2. Implementado CRUD completo para Transacciones
3. Organizado el código en modelos y enrutadores
4. Documentado con README simple

---

**Última actualización:** 27 de Mayo de 2026
