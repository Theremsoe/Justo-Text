""" A CreateValidation validation enclosure """

from masonite.validation import RuleEnclosure


class CreateValidation(RuleEnclosure):
    """A CreateValidation validation enclosure class."""

    def rules(self):
        return {
            "data.attributes": "required",
            "data.attributes.name": "required",
            "data.attributes.last_name": "required",
            "data.attributes.email": "required|emial",
            "data.attributes.username": "required",
            "data.attributes.password": "required|confirmed",
        }
