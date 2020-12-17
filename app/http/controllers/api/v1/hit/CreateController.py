"""A CreateController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.models import Hit
from app.http.resources.hit.HitResource import HitResource


class CreateController(Controller):
    """CreateController Controller Class."""

    def index(self, request: Request):
        pass
