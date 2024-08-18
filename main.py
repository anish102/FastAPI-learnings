from enum import Enum

from fastapi import FastAPI


# Enum class to define possible model names with specific string values
class ModelName(str, Enum):
    messi = "messi"
    sachin = "sachin"
    jordan = "jordan"


# Initialize the FastAPI application
app = FastAPI()


# Root endpoint that returns a simple "Hello World!" message
@app.get("/")
async def root():
    return {"message": "Hello World!"}


# Endpoint to handle dynamic file paths and return a confirmation message
@app.get("/files/{file_path:path}")
async def files(file_path):
    return {"message": "File received!"}


# Endpoint to return a message based on the provided model name
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.messi:
        return {"model_name": model_name, "message": "The GOAT of football"}
    if model_name.value == "sachin":
        return {"model_name": model_name, "message": "The GOAT of cricket"}
    if model_name is ModelName.jordan:
        return {"model_name": model_name, "message": "The GOAT of basketball"}


# Endpoint for path parameter as well as query parameters
@app.get("/items/{item_id}")
async def read_item(item_id: str, color: str | None = None, instock: bool = False):
    item = {"item_id": item_id}
    if color:
        item.update({"colort": color})
    if instock:
        item.update({"description": "Item is available"})
    return item
