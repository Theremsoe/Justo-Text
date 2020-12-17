from .HttpException import HttpException


class UnsupportedMediaTypeHttpException(HttpException):
    def __init__(self, message: str, headers: dict = {}, code: int = 0):
        super().__init__(415, message, headers=headers, code=code)
