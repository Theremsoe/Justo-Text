"""A ReadController Module."""

from masonite.controllers import Controller
from app.models.Target import Target
from app.http.responses.target.TargetResource import TargetResource


class ReadController(Controller):
    """ReadController Controller Class."""

    def index(self, id: int) -> TargetResource:
        return TargetResource(Target.find_or_fail(id))
