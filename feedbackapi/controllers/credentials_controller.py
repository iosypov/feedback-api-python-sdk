# -*- coding: utf-8 -*-

"""
feedbackapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from feedbackapi.api_helper import APIHelper
from feedbackapi.configuration import Server
from feedbackapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from feedbackapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from feedbackapi.models.credentials import Credentials
from feedbackapi.exceptions.unauthorized_exception import UnauthorizedException
from feedbackapi.exceptions.too_many_requests_exception import TooManyRequestsException
from feedbackapi.exceptions.internal_server_error_exception import InternalServerErrorException


class CredentialsController(BaseController):

    """A Controller to access Endpoints in the feedbackapi API."""
    def __init__(self, config):
        super(CredentialsController, self).__init__(config)

    def create_credentials(self):
        """Does a POST request to /credentials.

        ### Start here by creating your credentials
        Be careful to save the private key that is returned. You will not be
        able to retrieve it again.
        You can only have one private key at a time.
        Private key is not to be shared with anyone, do not expose it in your
        frontend code.

        Returns:
            Credentials: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/credentials')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Credentials.from_dictionary)
            .local_error('401', 'Unauthorized', UnauthorizedException)
            .local_error('429', 'Too Many Requests', TooManyRequestsException)
            .local_error('500', 'Internal Server Error', InternalServerErrorException)
        ).execute()

    def rotate_credentials(self,
                           x_api_key):
        """Does a PUT request to /credentials.

        ### Rotate credentials
        Generate a new private key and invalidate the current one.
        Use this in case your private key is compromised or for security
        reasons.

        Args:
            x_api_key (string): Private key. Create a tenant to generate.

        Returns:
            Credentials: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/credentials')
            .http_method(HttpMethodEnum.PUT)
            .header_param(Parameter()
                          .key('X-API-KEY')
                          .value(x_api_key))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Credentials.from_dictionary)
            .local_error('401', 'Unauthorized', UnauthorizedException)
            .local_error('429', 'Too Many Requests', TooManyRequestsException)
            .local_error('500', 'Internal Server Error', InternalServerErrorException)
        ).execute()

    def delete_credentials(self,
                           x_api_key):
        """Does a DELETE request to /credentials.

        ### Delete credentials
        Invalidate your current private key.
        You will no longer be able to create or read feedback.

        Args:
            x_api_key (string): Private key. Create a tenant to generate.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/credentials')
            .http_method(HttpMethodEnum.DELETE)
            .header_param(Parameter()
                          .key('X-API-KEY')
                          .value(x_api_key))
            .auth(Single('global'))
        ).execute()
