"""A ListController Module."""

from masonite.controllers import Controller
from masonite.request import Request
from app.http.responses.user_status.UserStatusCollection import UserStatusCollection
from app.models.UserStatus import UserStatus


class ListController(Controller):
    """ListController Controller Class."""

    def index(self, request: Request) -> UserStatusCollection:
        return UserStatusCollection(UserStatus.paginate())
