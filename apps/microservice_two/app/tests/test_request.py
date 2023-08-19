import pytest

from loguru import logger

from app.main import app

from fastapi.testclient import TestClient

from app.config.environment import get_environment_variables

env = get_environment_variables()

client = TestClient(app)

def test_microservice_up():
    response = client.get("/")
    assert response.status_code == 200
