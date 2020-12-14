"""A CreateController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.models.User import User
from masonite.request import Request
from app.rules.User.CreateValidation import CreateValidation


class CreateController(Controller):
    """CreateController Controller Class."""

    def index(self, request: Request):
        return User.create(request.validate(CreateValidation))
