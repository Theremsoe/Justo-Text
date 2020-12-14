"""Hit Model."""

from config.database import Model
from orator.orm import belongs_to
from orator.orm.relations import BelongsTo


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
    def user(self) -> BelongsTo:
        """ Get the user that must resolve hit. """
        from app.models.User import User

        return User

    @belongs_to("assigned_by_id")
    def assigned(self) -> BelongsTo:
        """ Get the user that assigned the hit. """
        from app.models.User import User

        return User

    @belongs_to
    def status(self) -> BelongsTo:
        """ Get the status that owns the hit status. """
        from app.models.HitStatus import HitStatus

        return HitStatus

    @belongs_to
    def target(self) -> BelongsTo:
        """ Get the target that owns the hit. """
        from app.models.Target import Target

        return Target
