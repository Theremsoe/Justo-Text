"""A ListController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.http.resources.target.TargetCollection import TargetCollection
from app.models import Target


class ListController(Controller):
    """ListController Controller Class."""

    def index(self, request: Request) -> TargetCollection:
        return TargetCollection(Target.paginate())
