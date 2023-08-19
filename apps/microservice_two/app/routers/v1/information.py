# FastApi
from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import JSONResponse
import time

microservice_one_router = APIRouter(
    prefix="",
    tags=["microservice_one"],
    responses={404: {"description": "Not found"}},
)

@microservice_one_router.get("/")
def home():
    content = {
        "message": "this is microservice TWO"
    }

    return JSONResponse(status_code=status.HTTP_200_OK, content=content)

@microservice_one_router.post("/")
def post():
    time.sleep(5)
    content = {
        "message" : "ok"
    }
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)
