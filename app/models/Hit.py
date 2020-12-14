"""Hit Model."""

from config.database import Model
from orator.orm import belongs_to
from app.models.HitStatus import HitStatus
from app.models.User import User
from app.models.Target import Target


class Hit(Model):
    """Hit Model."""

    __fillable__ = ["started_at", "expires_at"]

    __hidden__ = [
        "user_id",
        "assigned_by_id",
        "hit_status_id",
        "target_id",
    ]

    __casts__ = {
        "stared_at": "datetime",
        "expires_at": "datetime",
    }

    @belongs_to
    def user(self):
        return User

    @belongs_to("assigned_by_id")
    def assigned(self):
        return User

    @belongs_to
    def status(self):
        return HitStatus

    @belongs_to
    def target(self):
        return Target
