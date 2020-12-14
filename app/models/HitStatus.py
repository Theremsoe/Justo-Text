"""HitStatus Model."""

from config.database import Model
from orator.orm import has_many
from orator.orm.relations import HasMany


class HitStatus(Model):
    """HitStatus Model."""

    __table__ = "HIT_STATUS"

    __fillable__ = ["slug", "name", "details"]

    @has_many
    def hits(self) -> HasMany:
        """ Get the hits for the hit status. """
        from app.models.Hit import Hit

        return Hit
