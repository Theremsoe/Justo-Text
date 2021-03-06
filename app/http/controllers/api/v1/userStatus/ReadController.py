"""A ReadController Module."""

from masonite.controllers import Controller
from app.models import UserStatus
from app.http.resources.user_status.UserStatusResource import UserStatusResource


class ReadController(Controller):
    """ReadController Controller Class."""

    def index(self, id: int) -> UserStatusResource:
        return UserStatusResource(UserStatus.find_or_fail(id))
