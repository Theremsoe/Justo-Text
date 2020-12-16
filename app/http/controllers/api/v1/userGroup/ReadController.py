"""A ReadController Module."""

from masonite.controllers import Controller
from app.models.UserGroup import UserGroup
from app.http.responses.user_group.UserGroupResource import UserGroupResource


class ReadController(Controller):
    """ReadController Controller Class."""

    def index(self, id: int) -> UserGroupResource:
        return UserGroupResource(UserGroup.find_or_fail(id))
