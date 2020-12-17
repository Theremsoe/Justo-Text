from .HttpException import HttpException


class ServiceUnavailableHttpException(HttpException):
    def __init__(
        self,
        retry_after: int,
        message: str,
        headers: dict = {},
        code: int = 0,
    ):
        headers["Retry-After"] = retry_after
        super().__init__(503, message, headers=headers, code=code)
