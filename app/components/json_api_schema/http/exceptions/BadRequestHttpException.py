from .HttpException import HttpException


class BadRequestHttpException(HttpException):
    def __init__(self, message: str, headers: dict = {}, code: int = 0):
        super().__init__(400, message, headers=headers, code=code)
