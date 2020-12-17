from .HttpException import HttpException


class UnprocessableEntityHttpException(HttpException):
    def __init__(self, message: str, headers: dict = {}, code: int = 0):
        super().__init__(422, message, headers=headers, code=code)
