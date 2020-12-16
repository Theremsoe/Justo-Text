from app.http.responses.resources.json.ResourceCollection import ResourceCollection
from app.http.responses.hit_status.HitStatusResource import HitStatusResource


class HitStatusCollection(ResourceCollection):
    @property
    def collects(self) -> HitStatusResource:
        return HitStatusResource
