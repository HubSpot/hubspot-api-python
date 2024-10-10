# coding: utf-8

# flake8: noqa

"""
    Goal Targets

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from hubspot.crm.objects.goals.api.basic_api import BasicApi
from hubspot.crm.objects.goals.api.batch_api import BatchApi
from hubspot.crm.objects.goals.api.search_api import SearchApi

# import ApiClient
from hubspot.crm.objects.goals.api_client import ApiClient
from hubspot.crm.objects.goals.configuration import Configuration
from hubspot.crm.objects.goals.exceptions import OpenApiException
from hubspot.crm.objects.goals.exceptions import ApiTypeError
from hubspot.crm.objects.goals.exceptions import ApiValueError
from hubspot.crm.objects.goals.exceptions import ApiKeyError
from hubspot.crm.objects.goals.exceptions import ApiAttributeError
from hubspot.crm.objects.goals.exceptions import ApiException

# import models into sdk package
from hubspot.crm.objects.goals.models.associated_id import AssociatedId
from hubspot.crm.objects.goals.models.batch_read_input_simple_public_object_id import BatchReadInputSimplePublicObjectId
from hubspot.crm.objects.goals.models.batch_response_simple_public_object import BatchResponseSimplePublicObject
from hubspot.crm.objects.goals.models.batch_response_simple_public_object_with_errors import BatchResponseSimplePublicObjectWithErrors
from hubspot.crm.objects.goals.models.collection_response_associated_id import CollectionResponseAssociatedId
from hubspot.crm.objects.goals.models.collection_response_simple_public_object_with_associations_forward_paging import CollectionResponseSimplePublicObjectWithAssociationsForwardPaging
from hubspot.crm.objects.goals.models.collection_response_with_total_simple_public_object_forward_paging import CollectionResponseWithTotalSimplePublicObjectForwardPaging
from hubspot.crm.objects.goals.models.error import Error
from hubspot.crm.objects.goals.models.error_detail import ErrorDetail
from hubspot.crm.objects.goals.models.filter import Filter
from hubspot.crm.objects.goals.models.filter_group import FilterGroup
from hubspot.crm.objects.goals.models.forward_paging import ForwardPaging
from hubspot.crm.objects.goals.models.next_page import NextPage
from hubspot.crm.objects.goals.models.paging import Paging
from hubspot.crm.objects.goals.models.previous_page import PreviousPage
from hubspot.crm.objects.goals.models.public_object_search_request import PublicObjectSearchRequest
from hubspot.crm.objects.goals.models.simple_public_object import SimplePublicObject
from hubspot.crm.objects.goals.models.simple_public_object_id import SimplePublicObjectId
from hubspot.crm.objects.goals.models.simple_public_object_with_associations import SimplePublicObjectWithAssociations
from hubspot.crm.objects.goals.models.standard_error import StandardError
from hubspot.crm.objects.goals.models.value_with_timestamp import ValueWithTimestamp
