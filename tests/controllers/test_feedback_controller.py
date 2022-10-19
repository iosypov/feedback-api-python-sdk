# -*- coding: utf-8 -*-

"""
feedbackapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from feedbackapi.api_helper import APIHelper
from feedbackapi.models.feedback_req import FeedbackReq


class FeedbackControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(FeedbackControllerTests, cls).setUpClass()
        cls.controller = cls.client.feedback
        cls.response_catcher = cls.controller.http_call_back

    # ### Create a new feedback
    #You can explore sample payloads below.
    #Every feedback must have at least one properties:
    #  - `rating`: numeric value (star rating)
    #  - `sentiment`: boolean value (like/dislike button)
    #  - `reasons`: list of text values (multiple choice questions)
    #  - `suggestion`: text value (free text input)
    #
    #In addition, you may provide any of context values:
    #  - `userId`: string value (for logged in users, we'll generate one for anonymous users)
    #  - `page`: text value (url of the page where the feedback was given)
    #  - `category`: text value (category of the page where the feedback was given)
    #  - `apiOperationId`: text value (operationId for OpenAPI docs)
    #  - `tags`: list of text values (product name, feature name, etc.)
    #
    def test_create_feedback(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"rating":4,"suggestion":"Some screenshots would help","page":"htt'
            'ps://example.com/docs/tutorial/1","userId":"abc-xyz"}', FeedbackReq.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.create_feedback(body)

        # Test response code
        assert self.response_catcher.response.status_code == 201

        # Test headers
        expected_headers = {}
        expected_headers['set-cookie'] = None
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Update feedback by id.
    def test_update_feedback_by_id(self):
        # Parameters for the API call
        id = 'c73bcdcc-2669-4bf6-81d3-e4ae73fb11fd'
        body = APIHelper.json_deserialize('{"rating":4,"userId":"abc-xyz"}', FeedbackReq.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.update_feedback_by_id(id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


