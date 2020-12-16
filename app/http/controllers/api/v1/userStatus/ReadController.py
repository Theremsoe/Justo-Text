"""A ReadController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.models.UserStatus import UserStatus
from app.http.responses.user_status.UserStatusResource import UserStatusResource


class ReadController(Controller):
    """ReadController Controller Class."""

    def index(self, request: Request) -> UserStatusResource:
        return UserStatusResource(UserStatus.find_or_fail(request.param("id")))
