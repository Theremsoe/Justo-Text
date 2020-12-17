from masonite.response import Response
from app.http.resources.user_group.UserGroupResource import UserGroupResource


class UserGroupIdentifier(UserGroupResource):
    def dict_(self, response: Response) -> dict:
        return {
            "id": self.resource.id,
            "type": "user-group",
        }
