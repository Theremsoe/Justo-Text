"""UserGroup Model."""

from config.database import Model
from orator.orm import belongs_to_many
from app.models.User import User


class UserGroup(Model):
    """UserGroup Model."""

    __fillable__ = ["slug", "name", "details"]

    @belongs_to_many("USER_GROUP_LIST")
    def users(self):
        return User
