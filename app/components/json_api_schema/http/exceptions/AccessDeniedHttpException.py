from .HttpException import HttpException


class AccessDeniedHttpException(HttpException):
    def __init__(self, message: str, headers: dict = {}, code: int = 0):
        super().__init__(403, message, headers=headers, code=code)
