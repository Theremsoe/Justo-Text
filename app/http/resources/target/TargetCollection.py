from app.components.json_api_schema.http.schemas import ResourceCollection
from app.http.resources.target.TargetResource import TargetResource


class TargetCollection(ResourceCollection):
    @property
    def collects(self) -> TargetResource:
        return TargetResource
