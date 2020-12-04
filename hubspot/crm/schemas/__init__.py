# coding: utf-8

# flake8: noqa

"""
    Schemas

    The CRM uses schemas to define how custom objects should store and represent information in the HubSpot CRM. Schemas define details about an object's type, properties, and associations. The schema can be uniquely identified by its **object type ID**.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from hubspot.crm.schemas.api.core_api import CoreApi
from hubspot.crm.schemas.api.default_api import DefaultApi

# import ApiClient
from hubspot.crm.schemas.api_client import ApiClient
from hubspot.crm.schemas.configuration import Configuration
from hubspot.crm.schemas.exceptions import OpenApiException
from hubspot.crm.schemas.exceptions import ApiTypeError
from hubspot.crm.schemas.exceptions import ApiValueError
from hubspot.crm.schemas.exceptions import ApiKeyError
from hubspot.crm.schemas.exceptions import ApiException

# import models into sdk package
from hubspot.crm.schemas.models.association_definition import AssociationDefinition
from hubspot.crm.schemas.models.association_definition_egg import (
    AssociationDefinitionEgg,
)
from hubspot.crm.schemas.models.collection_response_object_schema import (
    CollectionResponseObjectSchema,
)
from hubspot.crm.schemas.models.error import Error
from hubspot.crm.schemas.models.error_detail import ErrorDetail
from hubspot.crm.schemas.models.model_property import ModelProperty
from hubspot.crm.schemas.models.next_page import NextPage
from hubspot.crm.schemas.models.object_schema import ObjectSchema
from hubspot.crm.schemas.models.object_schema_egg import ObjectSchemaEgg
from hubspot.crm.schemas.models.object_type_definition import ObjectTypeDefinition
from hubspot.crm.schemas.models.object_type_definition_labels import (
    ObjectTypeDefinitionLabels,
)
from hubspot.crm.schemas.models.object_type_definition_patch import (
    ObjectTypeDefinitionPatch,
)
from hubspot.crm.schemas.models.object_type_property_create import (
    ObjectTypePropertyCreate,
)
from hubspot.crm.schemas.models.option import Option
from hubspot.crm.schemas.models.option_input import OptionInput
from hubspot.crm.schemas.models.paging import Paging
from hubspot.crm.schemas.models.previous_page import PreviousPage
from hubspot.crm.schemas.models.property_modification_metadata import (
    PropertyModificationMetadata,
)
