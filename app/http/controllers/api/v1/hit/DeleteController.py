"""A DeleteController Module."""

from app.models.Hit import Hit
from app.http.responses.hit.HitResource import HitResource
from masonite.controllers import Controller


class DeleteController(Controller):
    """DeleteController Controller Class."""

    def index(self, id: int) -> HitResource:
        hit: Hit = Hit.find_or_fail(id)

        hit.delete()

        return HitResource(hit)
