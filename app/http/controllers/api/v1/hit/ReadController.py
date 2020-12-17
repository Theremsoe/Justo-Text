"""A ReadController Module."""

from app.models import Hit
from app.http.resources.hit.HitResource import HitResource
from masonite.controllers import Controller


class ReadController(Controller):
    """ReadController Controller Class."""

    def index(self, id: int) -> HitResource:
        return HitResource(Hit.find_or_fail(id))
