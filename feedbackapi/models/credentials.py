# -*- coding: utf-8 -*-

"""
feedbackapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Credentials(object):

    """Implementation of the 'Credentials' model.

    Credentials.

    Attributes:
        private_key (string): Private API Key.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "private_key": 'privateKey'
    }

    def __init__(self,
                 private_key=None):
        """Constructor for the Credentials class"""

        # Initialize members of the class
        self.private_key = private_key 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        private_key = dictionary.get("privateKey") if dictionary.get("privateKey") else None
        # Return an object of this model
        return cls(private_key)
