from app.http.responses.resources.json.JsonResource import JsonResource
from app.http.responses.user_status.UserStatusIdentifier import UserStatusIdentifier
from app.http.responses.user_group.UserGroupIdentifier import UserGroupIdentifier
from app.models.User import User
from masonite.response import Response


class UserResource(JsonResource):
    resource: User

    def __init__(self, resource: User):
        self.resource = resource

    def dict_(self, response: Response) -> dict:
        def status_relation() -> dict:
            return {
                "links": {
                    "self": route(
                        "api.v1.user-status.read", [self.resource.status.id], True
                    ),
                },
                "data": UserStatusIdentifier(self.resource.status).dict_(response),
            }

        def groups_relation() -> dict:
            return {
                "links": {"self": route("api.v1.user-group.list", [], True)},
                "data": UserGroupIdentifier.collection(self.resource.groups),
            }

        return {
            "id": self.resource.id,
            "type": "user",
            "attributes": {
                "name": self.resource.name,
                "last_name": self.resource.last_name,
                "email": self.resource.email,
                "username": self.resource.username,
                "created_at": str(self.resource.created_at),
                "updated_at": str(self.resource.updated_at),
                "deleted_at": self.when(
                    self.resource.deleted_at != None, str(self.resource.deleted_at)
                ),
            },
            "relationships": {
                "user_status": self.whenLoaded("status", status_relation),
                "user_group": self.whenLoaded("groups", groups_relation),
            },
            "links": {"self": route("api.v1.user.read", [self.resource.id], True)},
        }
