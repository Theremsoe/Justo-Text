"""A ListController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.models import UserGroup
from app.http.resources.user_group.UserGroupCollection import UserStatusCollection


class ListController(Controller):
    """ListController Controller Class."""

    def index(self, request: Request) -> UserStatusCollection:
        return UserStatusCollection(UserGroup.paginate())
