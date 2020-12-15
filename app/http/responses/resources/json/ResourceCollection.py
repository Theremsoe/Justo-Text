from app.http.responses.resources.json.JsonResource import JsonResource
from masonite.response import Response
from orator import LengthAwarePaginator, Collection


class ResourceCollection(JsonResource):
    def __init__(self, resource: LengthAwarePaginator):
        self.resource = resource

    def within(self, response: Response) -> dict:
        return {
            "links": {
                "first": "http://example.com",
                "last": "http://example.com",
                "prev": "http://example.com",
                "next": "http://example.com",
            }
        }

    @property
    def collects(self) -> JsonResource:
        return JsonResource

    def metadata(self, response: Response) -> dict:
        return {
            "metadata": {
                "total": self.resource.total,
                "count": self.resource.count(),
                "per_page": self.resource.per_page,
                "current_page": self.resource.current_page,
                "last_page": self.resource.last_page,
            }
        }

    def make_payload(self, response: Response) -> dict:
        items: Collection = self.resource.get_collection()

        return {
            **{self.wrapper: self.collects.collection(items)},
            **self.within(response),
            **self.metadata(response),
            **self.signature(response),
        }
