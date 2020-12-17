from app.components.json_api_schema.http.schemas import ResourceCollection
from app.http.resources.user_group.UserGroupResource import UserGroupResource


class UserStatusCollection(ResourceCollection):
    @property
    def collects(self) -> UserGroupResource:
        return UserGroupResource
