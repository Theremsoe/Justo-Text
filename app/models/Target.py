"""Target Model."""

from config.database import Model
from orator.orm import belongs_to
from app.models.Hit import Hit


class Target(Model):
    """Target Model."""

    __fillable__ = ["name", "last_name", "aka", "born_date"]

    __casts__ = {"born_date": "date"}

    @belongs_to
    def hits(self):
        return Hit
