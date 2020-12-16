from app.http.responses.resources.json.ResourceCollection import ResourceCollection
from app.http.responses.target.TargetResource import TargetResource


class TargetCollection(ResourceCollection):
    @property
    def collects(self) -> TargetResource:
        return TargetResource
