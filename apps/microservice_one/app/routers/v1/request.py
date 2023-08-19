# FastApi
from fastapi import APIRouter, Depends, Request, status, HTTPException
from fastapi.responses import JSONResponse
from loguru import logger

# cotrollers
from app.services.microservice_two import MicroserviceTwo

# schemas
from app.schemas.request import RequestSchema

# config
from app.config.environment import get_environment_variables

env = get_environment_variables()

request_router = APIRouter(
    prefix="",
    tags=["request"],
    responses={404: {"description": "Not found"}},
)

@request_router.get("/")
def home():
    content = {
        "message": "this is microservice ONE"
    }

    logger.info(f"This app its run in mode debug f{env.DEBUG}")

    return JSONResponse(status_code=status.HTTP_200_OK, content=content)

microservice_two = MicroserviceTwo()

@request_router.post("/")
async def send_request_microservice_two(data: RequestSchema):
    try:
        response = await microservice_two.send_request(data.dict())
        content = {
            "message": "Request successful",
            "response": response
        }
        return JSONResponse(status_code=202, content=content)
    except HTTPException as e:
        return str(e)

