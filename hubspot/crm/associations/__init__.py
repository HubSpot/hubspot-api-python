# flake8: noqa

"""
    Associations

    Associations define the relationships between objects in HubSpot. These endpoints allow you to create, read, and remove associations.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""



__version__ = "1.0.0"

# import apis into sdk package
from hubspot.crm.associations.api.batch_api import BatchApi
from hubspot.crm.associations.api.types_api import TypesApi

# import ApiClient
from hubspot.crm.associations.api_client import ApiClient
from hubspot.crm.associations.configuration import Configuration
from hubspot.crm.associations.exceptions import OpenApiException
from hubspot.crm.associations.exceptions import ApiTypeError
from hubspot.crm.associations.exceptions import ApiValueError
from hubspot.crm.associations.exceptions import ApiKeyError
from hubspot.crm.associations.exceptions import ApiException

# import models into sdk package
from hubspot.crm.associations.models.associated_id import AssociatedId
from hubspot.crm.associations.models.batch_input_public_association import (
    BatchInputPublicAssociation,
)
from hubspot.crm.associations.models.batch_input_public_object_id import (
    BatchInputPublicObjectId,
)
from hubspot.crm.associations.models.batch_response_public_association import (
    BatchResponsePublicAssociation,
)
from hubspot.crm.associations.models.batch_response_public_association_multi import (
    BatchResponsePublicAssociationMulti,
)
from hubspot.crm.associations.models.collection_response_public_association_definiton import (
    CollectionResponsePublicAssociationDefiniton,
)
from hubspot.crm.associations.models.error import Error
from hubspot.crm.associations.models.error_category import ErrorCategory
from hubspot.crm.associations.models.error_detail import ErrorDetail
from hubspot.crm.associations.models.next_page import NextPage
from hubspot.crm.associations.models.paging import Paging
from hubspot.crm.associations.models.public_association import PublicAssociation
from hubspot.crm.associations.models.public_association_definiton import (
    PublicAssociationDefiniton,
)
from hubspot.crm.associations.models.public_association_multi import (
    PublicAssociationMulti,
)
from hubspot.crm.associations.models.public_object_id import PublicObjectId
from hubspot.crm.associations.models.standard_error import StandardError
