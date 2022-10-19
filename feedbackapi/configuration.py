# -*- coding: utf-8 -*-

"""
feedbackapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from enum import Enum
from apimatic_core.http.configurations.http_client_configuration import HttpClientConfiguration
from apimatic_requests_client_adapter.requests_client import RequestsClient


class Environment(Enum):
    """An enum for SDK environments"""
    # Production server
    PRODUCTION = 0


class Server(Enum):
    """An enum for API servers"""
    DEFAULT = 0


class Configuration(HttpClientConfiguration):
    """A class used for configuring the SDK by a user.
    """

    @property
    def environment(self):
        return self._environment

    @property
    def x_rapid_api_key(self):
        return self._x_rapid_api_key

    def __init__(
        self, http_client_instance=None,
        override_http_client_configuration=False, http_call_back=None,
        timeout=60, max_retries=0, backoff_factor=2,
        retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
        retry_methods=['GET', 'PUT'], environment=Environment.PRODUCTION,
        x_rapid_api_key='TODO: Replace'
    ):
        super().__init__(http_client_instance, override_http_client_configuration, http_call_back, timeout, max_retries,
                         backoff_factor, retry_statuses, retry_methods)
        # Current API environment
        self._environment = environment

        # Your Rapid API Key
        self._x_rapid_api_key = x_rapid_api_key

        # The Http Client to use for making requests.
        super().set_http_client(self.create_http_client())

    def clone_with(self, http_client_instance=None,
                   override_http_client_configuration=None, http_call_back=None,
                   timeout=None, max_retries=None, backoff_factor=None,
                   retry_statuses=None, retry_methods=None, environment=None,
                   x_rapid_api_key=None):
        http_client_instance = http_client_instance or super().http_client_instance
        override_http_client_configuration = override_http_client_configuration or super().override_http_client_configuration
        http_call_back = http_call_back or super().http_callback
        timeout = timeout or super().timeout
        max_retries = max_retries or super().max_retries
        backoff_factor = backoff_factor or super().backoff_factor
        retry_statuses = retry_statuses or super().retry_statuses
        retry_methods = retry_methods or super().retry_methods
        environment = environment or self.environment
        x_rapid_api_key = x_rapid_api_key or self.x_rapid_api_key
        return Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment, x_rapid_api_key=x_rapid_api_key
        )

    def create_http_client(self):
        return RequestsClient(
            timeout=super().timeout, max_retries=super().max_retries,
            backoff_factor=super().backoff_factor, retry_statuses=super().retry_statuses,
            retry_methods=super().retry_methods,
            http_client_instance=super().http_client_instance,
            override_http_client_configuration=super().override_http_client_configuration,
            response_factory=super().http_response_factory
        )

    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.DEFAULT: 'https://feedback-api5.p.rapidapi.com/'
        }
    }

    def get_base_uri(self, server=Server.DEFAULT):
        """Generates the appropriate base URI for the environment and the
        server.

        Args:
            server (Configuration.Server): The server enum for which the base
            URI is required.

        Returns:
            String: The base URI.

        """
        return self.environments[self.environment][server]
