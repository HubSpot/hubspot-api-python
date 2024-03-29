# coding: utf-8

# flake8: noqa

"""
    Tags

    Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from hubspot.cms.blogs.tags.api.blog_tags_api import BlogTagsApi

# import ApiClient
from hubspot.cms.blogs.tags.api_client import ApiClient
from hubspot.cms.blogs.tags.configuration import Configuration
from hubspot.cms.blogs.tags.exceptions import OpenApiException
from hubspot.cms.blogs.tags.exceptions import ApiTypeError
from hubspot.cms.blogs.tags.exceptions import ApiValueError
from hubspot.cms.blogs.tags.exceptions import ApiKeyError
from hubspot.cms.blogs.tags.exceptions import ApiAttributeError
from hubspot.cms.blogs.tags.exceptions import ApiException

# import models into sdk package
from hubspot.cms.blogs.tags.models.attach_to_lang_primary_request_v_next import AttachToLangPrimaryRequestVNext
from hubspot.cms.blogs.tags.models.batch_input_json_node import BatchInputJsonNode
from hubspot.cms.blogs.tags.models.batch_input_string import BatchInputString
from hubspot.cms.blogs.tags.models.batch_input_tag import BatchInputTag
from hubspot.cms.blogs.tags.models.batch_response_tag import BatchResponseTag
from hubspot.cms.blogs.tags.models.batch_response_tag_with_errors import BatchResponseTagWithErrors
from hubspot.cms.blogs.tags.models.collection_response_with_total_tag_forward_paging import CollectionResponseWithTotalTagForwardPaging
from hubspot.cms.blogs.tags.models.detach_from_lang_group_request_v_next import DetachFromLangGroupRequestVNext
from hubspot.cms.blogs.tags.models.error import Error
from hubspot.cms.blogs.tags.models.error_detail import ErrorDetail
from hubspot.cms.blogs.tags.models.forward_paging import ForwardPaging
from hubspot.cms.blogs.tags.models.next_page import NextPage
from hubspot.cms.blogs.tags.models.set_new_language_primary_request_v_next import SetNewLanguagePrimaryRequestVNext
from hubspot.cms.blogs.tags.models.standard_error import StandardError
from hubspot.cms.blogs.tags.models.tag import Tag
from hubspot.cms.blogs.tags.models.tag_clone_request_v_next import TagCloneRequestVNext
from hubspot.cms.blogs.tags.models.update_languages_request_v_next import UpdateLanguagesRequestVNext
