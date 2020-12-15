"""A ReadController Module."""

from masonite.controllers import Controller
from app.models.User import User
from masonite.request import Request
from masonite.response import Response
from app.http.responses.user.UserResource import UserResource


class ReadController(Controller):
    """ReadController Controller Class."""

    def index(self, request: Request) -> UserResource:
        return UserResource(
            User.with_("status", "groups").find_or_fail(request.param("id"))
        )
