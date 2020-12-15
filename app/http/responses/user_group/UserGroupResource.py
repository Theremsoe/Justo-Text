from app.http.responses.resources.json.JsonResource import JsonResource
from app.models.UserGroup import UserGroup
from masonite.response import Response


class UserGroupResource(JsonResource):
    resource: UserGroup

    def __init__(self, resource: UserGroup):
        self.resource = resource

    def dict_(self, response: Response) -> dict:
        return {}
