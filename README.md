# Starlette API con MongoDB

Este proyecto es una API simple construida con **Starlette** y **MongoDB** utilizando el cliente **Motor**. La API permite realizar operaciones CRUD básicas para gestionar elementos (`items`) almacenados en una base de datos MongoDB. Además, la API incluye documentación generada automáticamente usando Swagger UI.

## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos principales:

- **main.py**: Configuración de la aplicación Starlette y definición de las rutas.
- **models.py**: Definición del modelo de datos `Item` utilizando Pydantic.
- **repositories.py**: Implementación del repositorio que maneja la interacción con la base de datos MongoDB.
- **services.py**: Implementación de la lógica de negocio para los `items`.
- **schemas.py**: Generación del esquema OpenAPI para la documentación de la API.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/DiegoLerma/starlette.git
    cd starlette
    ```

2. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

3. Asegúrate de que MongoDB esté instalado y ejecutándose en tu máquina, y que la dirección y puerto de MongoDB en `main.py` sean correctos:
    ```python
    client = AsyncIOMotorClient("mongodb://192.168.0.185:27017")
    ```

## Ejecución

Para ejecutar la aplicación:

```bash
uvicorn main:app --reload
```

La aplicación estará disponible en `http://127.0.0.1:8000`.

## Endpoints

### 1. Obtener Lista de Items

- **GET** `/items`
- **Descripción**: Devuelve una lista de todos los `items` almacenados en la base de datos.
- **Respuesta**: 
    - Código 200: Una lista de `items` en formato JSON.
    - Ejemplo de respuesta:
    ```json
    [
        {
            "id": "61b75e441ed1dc0d300a184a",
            "name": "Item 1",
            "description": "Descripción del item 1",
            "price": 19.99
        },
        {
            "id": "61b75e441ed1dc0d300a184b",
            "name": "Item 2",
            "description": "Descripción del item 2",
            "price": 29.99
        }
    ]
    ```

### 2. Crear un Nuevo Item

- **POST** `/items`
- **Descripción**: Crea un nuevo `item` en la base de datos.
- **Cuerpo de la petición**:
    ```json
    {
        "name": "Item 3",
        "description": "Descripción del item 3",
        "price": 9.99
    }
    ```
- **Respuesta**: 
    - Código 200: ID del `item` creado.
    - Ejemplo de respuesta:
    ```json
    {
        "id": "61b75e441ed1dc0d300a184c"
    }
    ```

### 3. Documentación de la API

- **GET** `/docs`
- **Descripción**: Muestra la documentación interactiva de la API generada automáticamente con Swagger UI.

- **GET** `/openapi.json`
- **Descripción**: Devuelve el esquema OpenAPI en formato JSON.

## Descripción de los Componentes

### 1. `Item` Modelo (models.py)

El modelo `Item` define la estructura de los datos de un `item`, incluyendo los siguientes campos:

- `id` (opcional): Identificador único del item.
- `name`: Nombre del item.
- `description` (opcional): Descripción del item.
- `price`: Precio del item.

### 2. Repositorio (repositories.py)

El `ItemRepository` maneja la interacción directa con la base de datos MongoDB, proporcionando métodos para agregar y obtener `items`.

### 3. Servicio (services.py)

El `ItemService` contiene la lógica de negocio para manipular los `items`. Actúa como intermediario entre los controladores (endpoints) y el repositorio.

### 4. Generación de Esquema (schemas.py)

El esquema OpenAPI se genera utilizando `SchemaGenerator` de Starlette. Este esquema se utiliza para crear la documentación de la API.

## Consideraciones Adicionales

- Asegúrate de ajustar la conexión a MongoDB en caso de que el servidor esté en una dirección IP o puerto diferente.
- La aplicación usa Swagger UI para la documentación interactiva, accesible en `/docs`.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor realiza un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está licenciado bajo la MIT License.
