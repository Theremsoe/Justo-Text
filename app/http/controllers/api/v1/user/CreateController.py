"""A CreateController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.models import User, UserStatus
from masonite.request import Request
from app.rules.user.CreateValidation import CreateValidation
from app.http.resources.user.UserResource import UserResource


class CreateController(Controller):
    """CreateController Controller Class."""

    def index(self, request: Request) -> UserResource:
        request.validate(CreateValidation)

        status: UserStatus = UserStatus.find_or_fail(
            request.input("data.relationships.user_status.id")
        )

        user: User = User(request.input("data.attributes"))
        user.status().associate(status)
        user.save()

        return UserResource(user)
