""" A CreateValidation validation enclosure """

from masonite.validation import (
    RuleEnclosure,
    required,
    email,
    strong,
    string,
    confirmed,
    numeric,
)


class CreateValidation(RuleEnclosure):
    """A CreateValidation validation enclosure class."""

    def rules(self):
        return [
            required(
                [
                    "data.attributes.name",
                    "data.attributes.username",
                    "data.attributes.email",
                    "data.attributes.password",
                    "data.relationships.user_status.id",
                ],
                raises=True,
            ),
            email(["data.attributes.email"], raises=True),
            string(["data.attributes.last_name"], raises=True),
            # Relationships validation
            numeric(["data.relationships.user_status.id"], raises=True),
        ]
