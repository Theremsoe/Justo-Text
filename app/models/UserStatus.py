"""UserStatus Model."""

from config.database import Model
from orator.orm import has_many
from app.models.User import User


class UserStatus(Model):
    """UserStatus Model."""

    """The attributes that are mass assignable."""
    __fillable__ = ["slug", "name", "details"]

    @has_many
    def users(self):
        return User
