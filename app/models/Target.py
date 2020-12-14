"""Target Model."""

from config.database import Model
from orator.orm import has_many
from orator.orm.relations import HasMany


class Target(Model):
    """Target Model."""

    __fillable__ = ["name", "last_name", "aka", "born_date"]

    __casts__ = {"born_date": "date"}

    @has_many
    def hits(self) -> HasMany:
        """ Get the hits for the target. """
        from app.models.Hit import Hit

        return Hit
