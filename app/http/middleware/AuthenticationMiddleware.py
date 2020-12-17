"""Authentication Middleware."""

from masonite.request import Request
from masonite.response import Response
from app.components.json_api_schema.http.schemas import ExceptionResource
from app.components.json_api_schema.http.exceptions import UnauthorizedHttpException


class AuthenticationMiddleware:
    """Middleware To Check If The User Is Logged In."""

    def __init__(self, request: Request, response: Response):
        """Inject Any Dependencies From The Service Container.

        Arguments:
            request {masonite.request.Request} -- The Masonite request class.
        """
        self.request = request
        self.response = response

    def before(self):
        """Run This Middleware Before The Route Executes."""
        if not self.request.user():
            raise UnauthorizedHttpException("Bearer", "An JWT token is required.")

    def after(self):
        """Run This Middleware After The Route Executes."""
        pass
