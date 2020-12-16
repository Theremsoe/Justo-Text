"""A ReadController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.models.Target import Target
from app.http.responses.target.TargetResource import TargetResource


class ReadController(Controller):
    """ReadController Controller Class."""

    def index(self, request: Request) -> TargetResource:
        return TargetResource(Target.find_or_fail(request.param("id")))
