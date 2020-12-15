from app.http.responses.user.UserResource import UserResource
from masonite.response import Response


class UserIdentifier(UserResource):
    def dict_(self, response: Response) -> dict:
        return {
            "id": self.resource.id,
            "type": "user",
        }
