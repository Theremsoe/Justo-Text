from app.http.responses.target.TargetResource import TargetResource
from masonite.response import Response


class TargetIdentifier(TargetResource):
    def dict_(self, response: Response) -> dict:
        return {"id": self.resource.id, "type": "target"}
