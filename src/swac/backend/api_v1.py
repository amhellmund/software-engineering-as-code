from fastapi import APIRouter

class BackendV1(APIRouter):
    def __init__(self):
        super().__init__()
        self._add_routes()

    def _add_routes(self):
        self.add_api_route("/requirements", self.get_requirements, methods=["GET"])

    def get_requirements(self):
        return []