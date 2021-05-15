# flake8: noqa

"""
    Visitor Identification

    The Visitor Identification API allows you to pass identification information to the HubSpot chat widget for otherwise unknown visitors that were verified by your own authentication system.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""



__version__ = "1.0.0"

# import apis into sdk package
from hubspot.conversations.visitor_identification.api.generate_api import GenerateApi

# import ApiClient
from hubspot.conversations.visitor_identification.api_client import ApiClient
from hubspot.conversations.visitor_identification.configuration import Configuration
from hubspot.conversations.visitor_identification.exceptions import OpenApiException
from hubspot.conversations.visitor_identification.exceptions import ApiTypeError
from hubspot.conversations.visitor_identification.exceptions import ApiValueError
from hubspot.conversations.visitor_identification.exceptions import ApiKeyError
from hubspot.conversations.visitor_identification.exceptions import ApiException

# import models into sdk package
from hubspot.conversations.visitor_identification.models.error import Error
from hubspot.conversations.visitor_identification.models.error_detail import ErrorDetail
from hubspot.conversations.visitor_identification.models.identification_token_generation_request import (
    IdentificationTokenGenerationRequest,
)
from hubspot.conversations.visitor_identification.models.identification_token_response import (
    IdentificationTokenResponse,
)
