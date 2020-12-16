from app.http.responses.resources.json.JsonResource import JsonResource
from app.models.UserStatus import UserStatus
from masonite.response import Response


class UserStatusResource(JsonResource):
    resource: UserStatus

    def __init__(self, resource: UserStatus):
        self.resource = resource

    def dict_(self, response: Response) -> dict:
        return {
            "id": self.resource.id,
            "type": "user-status",
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
            "relationhips": {
                "user": {
                    "links": {
                        "self": "https://localhost:8080:/api/v1/user-status/1/relationships/user"
                    }
                }
            },
            "links": {
                "self": route("api.v1.user-status.read", [self.resource.id], True)
            },
        }
