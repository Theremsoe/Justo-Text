""" A CreateValidation validation enclosure """

from masonite.validation import RuleEnclosure
from typing import List


class CreateValidation(RuleEnclosure):
    """A CreateValidation validation enclosure class."""

    def rules(self) -> List:
        return [
            # Rules go here
        ]
