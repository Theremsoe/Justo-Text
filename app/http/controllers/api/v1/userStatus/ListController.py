"""A ListController Module."""

from masonite.controllers import Controller
from masonite.request import Request
from app.http.resources.user_status.UserStatusCollection import UserStatusCollection
from app.models import UserStatus


class ListController(Controller):
    """ListController Controller Class."""

    def index(self, request: Request) -> UserStatusCollection:
        return UserStatusCollection(UserStatus.paginate())
