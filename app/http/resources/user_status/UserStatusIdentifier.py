from app.http.resources.user_status.UserStatusResource import UserStatusResource
from masonite.response import Response


class UserStatusIdentifier(UserStatusResource):
    def dict_(self, response: Response) -> dict:
        return {
            "id": self.resource.id,
            "type": "user-status",
        }
