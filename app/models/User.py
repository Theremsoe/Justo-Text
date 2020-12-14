"""User Model."""

from config.database import Model
from masonite.helpers import password
from orator.orm import belongs_to, belongs_to_many, has_many, mutator
from app.models.UserStatus import UserStatus
from app.models.UserGroup import UserGroup
from app.models.Hit import Hit


class User(Model):
    """User Model."""

    __fillable__ = ["name", "last_name", "email", "username", "password"]

    __hidden__ = ["user_status_id", "password"]

    __auth__ = "email"

    @mutator
    def password(self, value: str):
        self.set_raw_attribute("password", password("secret"))

    @belongs_to("user_status_id")
    def status(self):
        return UserStatus

    @belongs_to_many("USER_GROUP_LIST")
    def groups(self):
        return UserGroup

    @has_many
    def hits(self):
        return Hit

    @has_many("assigned_by_id")
    def assigned(self):
        return Hit
