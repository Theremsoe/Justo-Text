from app.components.json_api_schema.http.schemas import ResourceCollections
from app.http.resources.user.UserResource import UserResource


class UserCollection(ResourceCollection):
    @property
    def collects(self) -> UserResource:
        return UserResource
