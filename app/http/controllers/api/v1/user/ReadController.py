"""A ReadController Module."""

from masonite.controllers import Controller
from app.models import User
from app.http.resources.user.UserResource import UserResource


class ReadController(Controller):
    """ReadController Controller Class."""

    def index(self, id: int) -> UserResource:
        return UserResource(User.with_("status", "groups").find_or_fail(id))
