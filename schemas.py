from starlette.schemas import SchemaGenerator

schema_generator = SchemaGenerator(
    {
        "openapi": "3.0.0",
        "info": {"title": "Item API", "version": "1.0"},
        "paths": {
            "/items": {
                "get": {
                    "summary": "List Items",
                    "responses": {
                        "200": {
                            "description": "A list of items.",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "array",
                                        "items": {
                                            "$ref": "#/components/schemas/Item"
                                        },
                                    }
                                }
                            },
                        }
                    },
                },
                "post": {
                    "summary": "Create an Item",
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {"$ref": "#/components/schemas/Item"}
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "The ID of the created item.",
                            "content": {
                                "application/json": {
                                    "schema": {"type": "string"}
                                }
                            },
                        }
                    },
                },
            }
        },
        "components": {
            "schemas": {
                "Item": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "nullable": True},
                        "name": {"type": "string"},
                        "description": {"type": "string", "nullable": True},
                        "price": {"type": "number"},
                    },
                    "required": ["name", "price"],
                }
            }
        },
    }
)
