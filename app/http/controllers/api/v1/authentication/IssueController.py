"""A IssueControllerController Module."""

from masonite.request import Request
from masonite.auth import Auth
from masonite.controllers import Controller
from app.rules.authentication.IssueValidation import IssueValidation
from app.http.responses.user.UserResource import UserResource
from masonite.response import Response


class IssueController(Controller):
    """IssueController Controller Class."""

    def index(self, request: Request, auth: Auth, response: Response) -> UserResource:
        request.validate(IssueValidation)

        user: User = auth.login(request.input("login"), request.input("password"))

        if user:
            return UserResource(user)

        return response.json(
            {
                "errors": [
                    {
                        "status": "422",
                        "title": "Unprocessable Entity",
                        "detail": "Invalid credentials.",
                    }
                ]
            },
            422,
        )
