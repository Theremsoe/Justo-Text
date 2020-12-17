from app.components.json_api_schema.http.schemas import ResourceCollection
from app.http.resources.hit_status.HitStatusResource import HitStatusResource


class HitStatusCollection(ResourceCollection):
    @property
    def collects(self) -> HitStatusResource:
        return HitStatusResource
