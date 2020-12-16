"""A UpdateController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.models.User import User
from app.models.UserStatus import UserStatus
from app.http.responses.user.UserResource import UserResource
from app.rules.user.UpdateValidation import UpdateValidation


class UpdateController(Controller):
    """UpdateController Controller Class."""

    def index(self, id: int, request: Request) -> UserResource:
        request.validate(UpdateValidation)

        user: User = User.find_or_fail(id)
        status: UserStatus = UserStatus.find_or_fail(
            request.input("data.relationships.user_status.id")
        )

        user.fill(
            {
                "name": request.input("data.attributes.name"),
                "last_name": request.input("data.attributes.last_name"),
            }
        )
        user.status().associate(status)
        user.save()

        return UserResource(user)
