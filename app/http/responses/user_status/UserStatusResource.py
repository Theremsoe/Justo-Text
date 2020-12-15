from app.http.responses.resources.json.JsonResource import JsonResource
from app.models.UserStatus import UserStatus
from masonite.response import Response


class UserStatusResource(JsonResource):
    resource: UserStatus

    def __init__(self, resource: UserStatus):
        self.resource = resource

    def dict_(self, response: Response) -> dict:
        return {}
