from app.http.responses.resources.json.JsonResource import JsonResource
from app.models.HitStatus import HitStatus
from masonite.response import Response


class HitStatusResource(JsonResource):
    resource: HitStatus

    def __init__(self, resource: HitStatus):
        self.resource = resource

    def dict_(self, response: Response) -> dict:
        return {
            "id": self.resource.id,
            "type": "hit-status",
            "attributes": {
                "slug": self.resource.slug,
                "name": self.resource.name,
                "details": self.resource.details,
                "created_at": str(self.resource.created_at),
                "updated_at": str(self.resource.updated_at),
                "deleted_at": self.when(
                    self.resource.deleted_at != None, str(self.resource.deleted_at)
                ),
            },
            "relationships": {
                "hits": {
                    "links": {
                        "self": "http://localhost:8080/api/v1/hit-status/relationships/hit"
                    }
                }
            },
            "links": {
                "self": route("api.v1.hit-status.read", [self.resource.id], True)
            },
        }
