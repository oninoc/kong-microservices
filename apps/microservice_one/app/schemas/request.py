# fastapi
from pydantic import BaseModel

class RequestSchema(BaseModel):
    field_one: int
    field_two: str

    class Config:
        schema_extra = {
            "example" : {
                "field_one" : 22,
                "field_two" : 32,
            }
        }
