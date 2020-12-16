"""A ListController Module."""

from masonite.request import Request
from app.models.Hit import Hit
from app.http.responses.hit.HitCollection import HitCollection
from masonite.controllers import Controller


class ListController(Controller):
    """ListController Controller Class."""

    def index(self, request: Request) -> HitCollection:
        return HitCollection(Hit.paginate())
