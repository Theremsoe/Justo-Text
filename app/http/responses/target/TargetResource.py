from app.http.responses.resources.json.JsonResource import JsonResource
from app.models.Target import Target
from masonite.response import Response


class TargetResource(JsonResource):
    resource: Target

    def __init__(self, resource: Target):
        self.resource = resource

    def dict_(self, response: Response) -> dict:
        return {
            "id": self.resource.id,
            "type": "target",
            "attributes": {
                "name": self.resource.name,
                "last_name": self.resource.last_name,
                "aka": self.resource.aka,
                "born_data": self.when(
                    self.resource.born_data != None, str(self.resource.born_data)
                ),
                "created_at": str(self.resource.created_at),
                "updated_at": str(self.resource.updated_at),
                "deleted_at": self.when(
                    self.resource.deleted_at != None, str(self.resource.deleted_at)
                ),
            },
            "relationships": {
                "hits": {
                    "links": {
                        "self": "http://localhost:8080/api/v1/target/relationships/hit"
                    }
                }
            },
            "links": {"self": route("api.v1.target.read", [self.resource.id], True)},
        }
