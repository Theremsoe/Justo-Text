from app.components.json_api_schema.http.schemas import JsonResource
from app.models import UserGroup
from masonite.response import Response


class UserGroupResource(JsonResource):
    resource: UserGroup

    def __init__(self, resource: UserGroup):
        self.resource = resource

    def dict_(self, response: Response) -> dict:
        return {
            "id": self.resource.id,
            "type": "user-group",
            "attributes": {
                "slug": self.resource.slug,
                "name": self.resource.name,
                "details": self.resource.details,
                "level": self.resource.level,
                "created_at": str(self.resource.created_at),
                "updated_at": str(self.resource.updated_at),
                "deleted_at": self.when(
                    self.resource.deleted_at != None, str(self.resource.deleted_at)
                ),
            },
            "relationships": {
                "user": {
                    "links": {
                        "self": "https://localhost:8080:/api/v1/user-group/1/relationships/user"
                    }
                }
            },
            "links": {
                "self": route("api.v1.user-group.read", [self.resource.id], True)
            },
        }
