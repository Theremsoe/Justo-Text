from app.http.responses.resources.json.ResourceCollection import ResourceCollection
from app.http.responses.user_status.UserStatusResource import UserStatusResource


class UserStatusCollection(ResourceCollection):
    @property
    def collects(self) -> UserStatusResource:
        return UserStatusResource
