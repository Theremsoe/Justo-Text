"""A UpdateController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.models.Target import Target
from app.http.responses.target.TargetResource import TargetResource


class UpdateController(Controller):
    """UpdateController Controller Class."""

    def index(self, id: int, request: Request) -> TargetResource:
        target: Target = Target.find_or_fail(id)

        # target.fill({})

        return TargetResource(target)
