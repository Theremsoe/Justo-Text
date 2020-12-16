"""UserGroup Model."""

from config.database import Model
from orator.orm import belongs_to_many
from orator.orm.relations import BelongsToMany
from orator import SoftDeletes


class UserGroup(SoftDeletes, Model):
    """UserGroup Model."""

    __dates__ = ["deleted_at"]

    __table__ = "USER_GROUP"

    __fillable__ = ["slug", "name", "details", "level"]

    __casts__ = {"level": "integer"}

    @belongs_to_many("USER_GROUP_LIST", "user_group_id", "user_id")
    def users(self) -> BelongsToMany:
        """ The users that belong to the user group. """
        from app.models.User import User

        return User
