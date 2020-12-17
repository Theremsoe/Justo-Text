from .HttpException import HttpException


class NotFoundHttpException(HttpException):
    def __init__(self, message: str, headers: dict = {}, code: int = 0):
        super().__init__(404, message, headers=headers, code=code)
