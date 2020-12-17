from app.components.json_api_schema.http.schemas import ResourceCollection
from app.http.resources.hit.HitResource import HitResource


class HitCollection(ResourceCollection):
    @property
    def collects(self) -> HitResource:
        return HitResource
