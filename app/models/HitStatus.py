"""HitStatus Model."""

from config.database import Model
from orator.orm import has_many
from app.models.Hit import Hit


class HitStatus(Model):
    """HitStatus Model."""

    __fillable__ = ["slug", "name", "details"]

    @has_many
    def hits(self):
        return Hit
