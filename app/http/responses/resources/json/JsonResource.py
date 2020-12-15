from masonite.response import Responsable
from masonite.response import Response
from masonite import app
from orator import Collection
from typing import Callable, List


class JsonResource(Responsable):
    wrapper: str = "data"

    def __init__(self, resource):
        self.resource = resource

    @classmethod
    def collection(cls, items: Collection) -> List:
        response: Response = request().app().resolve(Response)

        return items.map(lambda item: cls(item).dict_(response)).all()

    def dict_(self, response: Response) -> dict:
        return {}

    def within(self, response: Response) -> dict:
        return {}

    def metadata(self, response: Response) -> dict:
        return {}

    def signature(self, response: Response) -> dict:
        """ JSON API Sigunature """
        return {"jsonapi": {"version": "1.1"}}

    def when(self, condition: bool, value, default=None):
        """ Retrieve a value based on a given condition. """
        if condition:
            return value() if isinstance(value, Callable) else value

        return default

    def whenLoaded(self, relation: str, value, default=None):
        """ Retrieve a relationship if it has been loaded. """
        return self.when(relation in self.resource._relations, value, default)

    def make_payload(self, response: Response) -> dict:
        return {
            **{self.wrapper: self.dict_(response)},
            **self.within(response),
            **self.metadata(response),
            **self.signature(response),
        }

    def get_response(self) -> str:
        response: Response = request().app().resolve(Response)

        response.request.header("Content-Type", "application/vnd.api+json")

        return response.json(self.make_payload(response))
