from .HttpException import HttpException


class UnauthorizedHttpException(HttpException):
    def __init__(
        self,
        challenge: str,
        message: str,
        headers: dict = {},
        code: int = 0,
    ):
        headers["WWW-Authenticate"] = challenge
        super().__init__(401, message, headers=headers, code=code)
