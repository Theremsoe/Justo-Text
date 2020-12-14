"""A ListController Module."""

from masonite.controllers import Controller
from app.models.User import User


class ListController(Controller):
    """ListController Controller Class."""

    def index(self):
        return User.paginate()
