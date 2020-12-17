from .HttpException import HttpException


class ConflictHttpException(HttpException):
    def __init__(self, message: str, headers: dict = {}, code: int = 0):
        super().__init__(409, message, headers=headers, code=code)
