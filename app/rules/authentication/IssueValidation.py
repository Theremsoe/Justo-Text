""" A IssueValidation validation enclosure """

from masonite.validation import RuleEnclosure, required
from typing import List


class IssueValidation(RuleEnclosure):
    """A IssueValidation validation enclosure class."""

    def rules(self) -> List:
        return [required(["login", "password"], raises=True)]
