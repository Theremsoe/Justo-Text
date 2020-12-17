from app.http.resources.hit_status.HitStatusResource import HitStatusResource
from masonite.response import Response


class HitStatusIdentifier(HitStatusResource):
    def dict_(self, response: Response) -> dict:
        return {
            "id": self.resource.id,
            "type": "hit-status",
        }
