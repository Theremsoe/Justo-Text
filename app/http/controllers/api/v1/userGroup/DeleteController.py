"""A DeleteController Module."""

from masonite.request import Request
from masonite.controllers import Controller
from app.models.UserGroup import UserGroup
from app.http.responses.user_group.UserGroupResource import UserGroupResource


class DeleteController(Controller):
    """DeleteController Controller Class."""

    def index(self, request: Request) -> UserGroupResource:
        group: UserGroup = UserGroup.find_or_fail(request.param("id"))

        group.delete()

        return UserGroupResource(group)
