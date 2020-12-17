import uuid
import pendulum
from masonite.response import Response


class HttpException(Exception):
    """ Http Exception. """

    __status_code: int
    """ Http code. """

    __message: str
    """ Http exception. """

    __headers: dict
    """ Http extra headers. """

    __code: int
    """ Exception code. """

    __id: str
    """ Exception Identifier. """

    __timestamp: str
    """ Exception timestamp. """

    def __init__(
        self, status_code: int, message: str, headers: dict = {}, code: int = 0
    ):
        super().__init__(message)
        self.__status_code = status_code
        self.__message = message
        self.__headers = headers
        self.__code = code
        self.__id = str(uuid.uuid4())
        self.__timestamp = str(pendulum.utcnow())

    def get_status_code(self) -> int:
        return self.__status_code

    def get_headers(self) -> dict:
        return self.__headers

    def set_headers(self, headers: dict) -> None:
        self.__headers = headers

    def get_code(self) -> int:
        return self.__code

    def get_id(self) -> str:
        return self.__id

    def get_timestamp(self) -> str:
        return self.__timestamp
