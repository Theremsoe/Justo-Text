from app.http.responses.resources.json.ResourceCollection import ResourceCollection
from app.http.responses.hit.HitResource import HitResource


class HitCollection(ResourceCollection):
    @property
    def collects(self) -> HitResource:
        return HitResource
