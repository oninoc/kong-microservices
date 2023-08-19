from fastapi import FastAPI
from app.middlewares.error_handler import ErrorHandler
from app.routers.v1.request import request_router

app = FastAPI(
            swagger_ui_parameters={"tryItOutEnabled": True},
              )
app.title = "Microservice ONE"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

app.include_router(request_router)
