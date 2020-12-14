"""A CreateController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class CreateController(Controller):
    """CreateController Controller Class."""

    def __init__(self, request: Request):
        """CreateController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        pass
