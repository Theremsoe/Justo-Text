from masonite.request import Request
from masonite.response import Response
from ..exceptions.HttpException import HttpException
from ..schemas.ExceptionResource import ExceptionResource


class ExceptionHandler:
    def __init__(self, request: Request):
        self.request = request

    def handle(self, exception: Exception):
        return ExceptionResource(exception).get_response()
