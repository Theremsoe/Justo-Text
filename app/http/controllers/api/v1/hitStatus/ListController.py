"""A ListController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.models.HitStatus import HitStatus
from app.http.responses.hit_status.HitStatusCollection import HitStatusCollection


class ListController(Controller):
    """ListController Controller Class."""

    def index(self, request: Request) -> HitStatusCollection:
        return HitStatusCollection(HitStatus.paginate())
