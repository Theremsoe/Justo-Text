from app.http.responses.resources.json.JsonResource import JsonResource
from app.models.Hit import Hit
from masonite.response import Response


class HitResource(JsonResource):
    resource: Hit

    def __init__(self, resource: Hit):
        self.resource = resource

    def dict_(self, response: Response) -> dict:
        return {
            "id": self.resource.id,
            "type": "hit",
            "attributes": {
                "stared_at": str(self.resource.stared_at),
                "expires_at": str(self.resource.expires_at),
                "details": self.resource.details,
                "created_at": str(self.resource.created_at),
                "updated_at": str(self.resource.updated_at),
                "deleted_at": self.when(
                    self.resource.deleted_at != None, str(self.resource.deleted_at)
                ),
            },
            "relationships": {
                "user": {
                    "links": {
                        "self": route(
                            "api.v1.user.read", [self.resource.user_id], True
                        ),
                    },
                    "data": {},
                },
                "assigned": {
                    "links": {
                        "self": route(
                            "api.v1.user.read", [self.resource.assigned_by_id], True
                        ),
                    },
                    "data": {},
                },
                "status": {
                    "links": {
                        "self": route(
                            "api.v1.hit-status.read",
                            [self.resource.hit_status_id],
                            True,
                        ),
                    },
                    "data": {},
                },
                "target": {
                    "links": {
                        "self": route(
                            "api.v1.target.read", [self.resource.target_id], True
                        ),
                    },
                    "data": {},
                },
            },
            "links": {"self": route("api.v1.hit.read", [self.resource.id], True)},
        }
