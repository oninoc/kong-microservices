from app.services.microservice_two import MicroserviceTwo

class RequestController:
    def __init__(self) -> None:
        self.mst = MicroserviceTwo()

    def get_request(self, data: dict) -> dict:
        return self.mst.send_request_microservice_two(data)
