"""User Model."""

from config.database import Model
from masonite.helpers import password
from orator.orm import belongs_to, belongs_to_many, has_many, mutator
from orator.orm.relations import BelongsToMany, BelongsTo, HasMany


class User(Model):
    """User Model."""

    __table__ = "USER"

    __fillable__ = ["name", "last_name", "email", "username", "password"]

    __hidden__ = ["user_status_id", "password"]

    __auth__ = "email"

    @mutator
    def password(self, value: str) -> None:
        """ Set the user password. """
        self.set_raw_attribute("password", password("secret"))

    @belongs_to("user_status_id")
    def status(self) -> BelongsTo:
        """ Get the user status that owns the user. """
        from app.models.UserStatus import UserStatus

        return UserStatus

    @belongs_to_many("USER_GROUP_LIST", "user_id", "user_group_id")
    def groups(self) -> BelongsToMany:
        """ The groups that belong to the user. """
        from app.models.UserGroup import UserGroup

        return UserGroup

    @has_many
    def hits(self) -> HasMany:
        """ Get the hits for the user. """
        from app.models.Hit import Hit

        return Hit

    @has_many("assigned_by_id")
    def assigned(self) -> HasMany:
        """ Get the hits for the user that assigned. """
        from app.models.Hit import Hit

        return Hit
