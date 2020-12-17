from .JsonResource import JsonResource
from masonite.request import Request
from orator import LengthAwarePaginator, Collection


class ResourceCollection(JsonResource):
    def __init__(self, resource: LengthAwarePaginator):
        self.resource = resource

    @property
    def collects(self) -> JsonResource:
        """ The resource that this resource collects. """
        return JsonResource

    def within(self, request: Request) -> dict:
        return {
            "links": {
                "first": "http://example.com",
                "last": "http://example.com",
                "prev": "http://example.com",
                "next": "http://example.com",
            }
        }

    def additional(self, request: Request):
        original: dict = super().additional(request)

        return {
            **original,
            "metadata": {
                "total": self.resource.total,
                "count": self.resource.count(),
                "per_page": self.resource.per_page,
                "current_page": self.resource.current_page,
                "last_page": self.resource.last_page,
            },
        }

    def resolve(self, request: Request) -> dict:
        """ Resolve the resource to a dictionary."""
        return {self.wrapper: self.collects.collection(self.resource.get_collection())}
