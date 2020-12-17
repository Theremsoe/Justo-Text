from masonite.response import Responsable, Response
from masonite.request import Request
from orator import Collection
from typing import Callable, List
from masonite.app import App
import json


class JsonResource(Responsable):

    wrapper: str = "data"
    """ The "data" wrapper that should be applied. """

    def __init__(self, resource):
        self.resource = resource

    @classmethod
    def collection(cls, items: Collection) -> List:
        """  Create new anonymous resource collection. """
        request: Request = request()

        return items.map(lambda item: cls(item).dict_(request)).all()

    def dict_(self, request: Request) -> dict:
        return {}

    def within(self, request: Request) -> dict:
        """ Get any additional data that should be returned with the resource array. """
        return {}

    def additional(self, request: Request) -> dict:
        """ Add additional meta data to the resource response. """
        return {"jsonapi": {"version": "1.1"}}

    def resolve(self, request: Request) -> dict:
        """ Resolve the resource to an array."""
        return {self.wrapper: self.dict_(request)}

    def when(self, condition: bool, value, default=None):
        """ Retrieve a value based on a given condition. """
        if condition:
            return value() if isinstance(value, Callable) else value

        return default

    def whenLoaded(self, relation: str, value, default=None):
        """ Retrieve a relationship if it has been loaded. """
        return self.when(relation in self.resource._relations, value, default)

    def payload(self, request: Request) -> dict:
        return {
            **self.resolve(request),
            **self.within(request),
            **self.additional(request),
        }

    def get_response(self) -> str:
        req: Request = request()
        app: App = req.app()
        res: Response = app.make(Response)

        req.status(200)

        # Set JSON Payload response
        app.bind("Response", bytes(json.dumps(self.payload(req)), "utf-8"))

        if not req.has_raw_header("Content-Type"):
            req.header("Content-Type", "application/vnd.api+json")

        req.header("Content-Length", str(len(res.data())))

        return res.data()
