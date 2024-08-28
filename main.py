from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse
from starlette.routing import Route
from motor.motor_asyncio import AsyncIOMotorClient
from services import ItemService
from repositories import ItemRepository
from models import Item
import uvicorn
from starlette.endpoints import HTTPEndpoint
from schemas import schema_generator  # Importar el esquema desde schemas.py

# Inicializar la base de datos
client = AsyncIOMotorClient("mongodb://127.0.0.1:27017")
database = client.starlette_api

# Inicializar el repositorio y servicio
item_repository = ItemRepository(database)
item_service = ItemService(item_repository)


class ItemList(HTTPEndpoint):
    async def get(self, request):
        """Get list of items"""
        items = await item_service.get_items()
        return JSONResponse([item.dict() for item in items])

    async def post(self, request):
        """Create a new item"""
        data = await request.json()
        item = Item(**data)
        item_id = await item_service.add_item(item)
        return JSONResponse({"id": item_id})


# Rutas de la aplicación
routes = [
    Route("/items", ItemList),
    Route("/openapi.json", lambda request: JSONResponse(schema_generator.get_schema(routes))),
    Route("/docs", lambda request: HTMLResponse(
        """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Swagger UI</title>
            <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.15.5/swagger-ui.css" />
            <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.15.5/swagger-ui-bundle.js"> </script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/4.15.5/swagger-ui-standalone-preset.js"> </script>
            <script>
            window.onload = function() {
                const ui = SwaggerUIBundle({
                    url: '/openapi.json',
                    dom_id: '#swagger-ui',
                    presets: [
                        SwaggerUIBundle.presets.apis,
                        SwaggerUIStandalonePreset
                    ],
                    layout: "StandaloneLayout"
                })
                window.ui = ui
            }
            </script>
        </head>
        <body>
            <div id="swagger-ui"></div>
        </body>
        </html>
        """
    )),
]

app = Starlette(routes=routes)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
