from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.5])

    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "name": "Foo",
    #                 "description": "A very nice Item",
    #                 "price": 35.4,
    #                 "tax": 3.2,
    #             }
    #         ]
    #     }
    # }


class Category(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/categories/{category_id}")
async def update_category(
    category_id: int,
    category: Annotated[
        Category,
        Body(
            examples=[
                {
                    "name": "Sports",
                    "description": "A very nice category",
                    "price": 45.3,
                    "tax": 3.8,
                }
            ],
        ),
    ],
):
    results = {"category_id": category_id, "category": category}
    return results
