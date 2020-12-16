"""A UpdateController Module."""

from masonite.request import Request
from app.models.Hit import Hit
from app.http.responses.hit.HitResource import HitResource
from masonite.controllers import Controller


class UpdateController(Controller):
    """UpdateController Controller Class."""

    def index(self, id: int, request: Request) -> HitResource:
        hit: Hit = Hit.find_or_fail(id)

        # hit.fill({})

        return HitResource(hit)
