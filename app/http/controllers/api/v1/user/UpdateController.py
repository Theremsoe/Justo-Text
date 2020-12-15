"""A UpdateController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.models.User import User
from app.http.responses.user.UserResource import UserResource


class UpdateController(Controller):
    """UpdateController Controller Class."""

    def index(self, request: Request) -> UserResource:
        user: User = User.find_or_fail(request.param("id"))

        return UserResource(user)
