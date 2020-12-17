from .JsonResource import JsonResource
from ..exceptions.HttpException import HttpException
from masonite.request import Request
from masonite.helpers.status import response_statuses


class ExceptionResource(JsonResource):
    wrapper: str = "errors"
    """ The "data" wrapper that should be applied. """

    def __init__(self, resource: HttpException):
        self.resource = resource

    def dict_(self, request: Request):
        request.status(self.resource.get_status_code())
        request.header(self.resource.get_headers())

        return {
            "id": self.resource.get_id(),
            "status": self.resource.get_status_code(),
            "code": self.resource.get_code(),
            "title": response_statuses()[self.resource.get_status_code()],
            "detail": str(self.resource),
            "meta": {
                "timestamp": self.resource.get_timestamp(),
            },
        }
