"""A ReadController Module."""

from masonite.controllers import Controller
from app.models.User import User
from masonite.request import Request


class ReadController(Controller):
    """ReadController Controller Class."""

    def index(self, request: Request):
        return User.find_or_fail(request.param("id"))
