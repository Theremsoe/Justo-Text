from app.http.responses.resources.json.ResourceCollection import ResourceCollection
from app.http.responses.user.UserResource import UserResource


class UserCollection(ResourceCollection):
    @property
    def collects(self) -> UserResource:
        return UserResource
