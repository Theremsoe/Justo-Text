from app.http.responses.resources.json.ResourceCollection import ResourceCollection
from app.http.responses.user_group.UserGroupResource import UserGroupResource


class UserStatusCollection(ResourceCollection):
    @property
    def collects(self) -> UserGroupResource:
        return UserGroupResource
