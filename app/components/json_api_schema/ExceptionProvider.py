from masonite.provider import ServiceProvider
from .http.handler.ExceptionHandler import ExceptionHandler


class ExceptionProvider(ServiceProvider):
    """ Binds the User model into the Service Container """

    wsgi = False

    def register(self):
        self.app.bind("ExceptionUnauthorizedHttpExceptionHandler", ExceptionHandler)

    def boot(self):
        pass
