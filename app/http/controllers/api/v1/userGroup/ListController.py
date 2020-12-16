"""A ListController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.models.UserGroup import UserGroup
from app.http.responses.user_group.UserGroupCollection import UserStatusCollection


class ListController(Controller):
    """ListController Controller Class."""

    def index(self, request: Request) -> UserStatusCollection:
        return UserStatusCollection(UserGroup.paginate())
