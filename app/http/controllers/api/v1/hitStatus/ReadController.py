"""A ReadController Module."""

from masonite.controllers import Controller
from app.models.HitStatus import HitStatus
from app.http.responses.hit_status.HitStatusResource import HitStatusResource


class ReadController(Controller):
    """ReadController Controller Class."""

    def index(self, id: int) -> HitStatusResource:
        return HitStatusResource(HitStatus.find_or_fail(id))
