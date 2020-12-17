from app.http.resources.hit.HitResource import HitResource
from masonite.response import Response


class HitIdentifier(HitResource):
    def dict_(self, response: Response) -> dict:
        return {
            "id": self.resource.id,
            "type": "hit",
        }
