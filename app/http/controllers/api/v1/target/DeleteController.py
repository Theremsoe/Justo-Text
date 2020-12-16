"""A DeleteController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.models.Target import Target
from app.http.responses.target.TargetResource import TargetResource


class DeleteController(Controller):
    """DeleteController Controller Class."""

    def index(self, request: Request) -> TargetResource:
        target: Target = Target.find_or_fail(request.param("id"))

        target.delete()

        return TargetResource(target)
