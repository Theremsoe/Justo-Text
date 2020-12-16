"""A ReadController Module."""

from masonite.controllers import Controller
from app.models.User import User
from app.http.responses.user.UserResource import UserResource


class ReadController(Controller):
    """ReadController Controller Class."""

    def index(self, id: int) -> UserResource:
        return UserResource(User.with_("status", "groups").find_or_fail(id))
