# -*- coding: utf-8 -*-

"""
feedbackapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from feedbackapi.api_helper import APIHelper
from feedbackapi.models.feedback import Feedback
from feedbackapi.models.pagination import Pagination


class FeedbackResponse(object):

    """Implementation of the 'Feedback Response' model.

    TODO: type model description here.

    Attributes:
        data (list of Feedback): TODO: type description here.
        pagination (Pagination): Pagination object.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": 'data',
        "pagination": 'pagination'
    }

    _optionals = [
        'data',
        'pagination',
    ]

    def __init__(self,
                 data=APIHelper.SKIP,
                 pagination=APIHelper.SKIP):
        """Constructor for the FeedbackResponse class"""

        # Initialize members of the class
        if data is not APIHelper.SKIP:
            self.data = data 
        if pagination is not APIHelper.SKIP:
            self.pagination = pagination 

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

        data = None
        if dictionary.get('data') is not None:
            data = [Feedback.from_dictionary(x) for x in dictionary.get('data')]
        else:
            data = APIHelper.SKIP
        pagination = Pagination.from_dictionary(dictionary.get('pagination')) if 'pagination' in dictionary.keys() else APIHelper.SKIP 
        # Return an object of this model
        return cls(data,
                   pagination)