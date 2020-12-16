""" A UpdateValidation validation enclosure """

from masonite.validation import RuleEnclosure
from typing import List


class UpdateValidation(RuleEnclosure):
    """A UpdateValidation validation enclosure class."""

    def rules(self) -> List:
        return [
            # Rules go here
        ]
