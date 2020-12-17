from app.components.json_api_schema.http.schemas import ResourceCollection
from app.http.resources.user_status.UserStatusResource import UserStatusResource


class UserStatusCollection(ResourceCollection):
    @property
    def collects(self) -> UserStatusResource:
        return UserStatusResource
