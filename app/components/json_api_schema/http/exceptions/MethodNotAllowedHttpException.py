from .HttpException import HttpException
from typing import List, Callable


class MethodNotAllowedHttpException(HttpException):
    def __init__(
        self,
        allow: List[str],
        message: str,
        headers: dict = {},
        code: int = 0,
    ):
        upper_callable: Callable[[str], str] = lambda method: method.upper()

        headers["Allow"] = ", ".join(allow.map(upper_callable))

        super().__init__(405, message, headers=headers, code=code)
