""" A UpdateValidation validation enclosure """

from masonite.validation import RuleEnclosure, required, numeric, string, email
from typing import List


class UpdateValidation(RuleEnclosure):
    """A UpdateValidation validation enclosure class."""

    def rules(self) -> List:
        return [
            required(
                [
                    "data.attributes.name",
                    "data.attributes.username",
                    "data.attributes.email",
                    "data.relationships.user_status.id",
                ],
                raises=True,
            ),
            email(["data.attributes.email"], raises=True),
            string(["data.attributes.last_name"], raises=True),
            numeric(["data.relationships.user_status.id"], raises=True),
        ]
