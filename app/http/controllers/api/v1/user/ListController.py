"""A ListController Module."""

from masonite.controllers import Controller
from app.models import User
from app.http.resources.user.UserCollection import UserCollection
from masonite.request import Request


class ListController(Controller):
    """ListController Controller Class."""

    def index(self, request: Request) -> UserCollection:
        return UserCollection(User.paginate())
