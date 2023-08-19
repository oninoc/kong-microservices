import httpx
from loguru import logger
from fastapi import HTTPException

class MicroserviceTwo:
    def __init__(self) -> None:
        pass

    async def send_request(self, data: dict) -> dict:
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.post('http://microservice_two', json=data)
                response.raise_for_status()
                response_data = response.json()
                logger.info(response_data)
                return response_data
        except httpx.HTTPError as e:
            logger.error(f"HTTP error: {str(e)}")

