"""A DeleteController Module."""

from masonite.controllers import Controller
from app.models import Target
from app.http.resources.target.TargetResource import TargetResource


class DeleteController(Controller):
    """DeleteController Controller Class."""

    def index(self, id: int) -> TargetResource:
        target: Target = Target.find_or_fail(id)

        target.delete()

        return TargetResource(target)
