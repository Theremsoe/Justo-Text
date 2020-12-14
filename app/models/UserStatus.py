"""UserStatus Model."""

from config.database import Model
from orator.orm import has_many
from orator.orm.relations import HasMany


class UserStatus(Model):
    """UserStatus Model."""

    __table__ = "USER_STATUS"

    """The attributes that are mass assignable."""
    __fillable__ = ["slug", "name", "details"]

    @has_many("user_status_id")
    def users(self) -> HasMany:
        """ Get all of the users for the user status. """
        from app.models.User import User

        return User
