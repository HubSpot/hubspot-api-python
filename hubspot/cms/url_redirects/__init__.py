# flake8: noqa

"""
    URL redirects

    URL redirect operations  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""



__version__ = "1.0.0"

# import apis into sdk package
from hubspot.cms.url_redirects.api.redirects_api import RedirectsApi

# import ApiClient
from hubspot.cms.url_redirects.api_client import ApiClient
from hubspot.cms.url_redirects.configuration import Configuration
from hubspot.cms.url_redirects.exceptions import OpenApiException
from hubspot.cms.url_redirects.exceptions import ApiTypeError
from hubspot.cms.url_redirects.exceptions import ApiValueError
from hubspot.cms.url_redirects.exceptions import ApiKeyError
from hubspot.cms.url_redirects.exceptions import ApiException

# import models into sdk package
from hubspot.cms.url_redirects.models.collection_response_with_total_url_mapping import (
    CollectionResponseWithTotalUrlMapping,
)
from hubspot.cms.url_redirects.models.error import Error
from hubspot.cms.url_redirects.models.error_detail import ErrorDetail
from hubspot.cms.url_redirects.models.next_page import NextPage
from hubspot.cms.url_redirects.models.paging import Paging
from hubspot.cms.url_redirects.models.url_mapping import UrlMapping
from hubspot.cms.url_redirects.models.url_mapping_create_request_body import (
    UrlMappingCreateRequestBody,
)
