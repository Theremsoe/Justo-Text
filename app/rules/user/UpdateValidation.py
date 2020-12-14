""" A UpdateValidation validation enclosure """

from masonite.validation import RuleEnclosure


class UpdateValidation(RuleEnclosure):
    """A UpdateValidation validation enclosure class.
    """

    def rules(self):
        """Used to return a list of rules in order to make some validation
        more reusable.
        
        Returns:
            list -- List of rules
        """
        return [
            # Rules go here
        ]