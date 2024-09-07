# coding: utf-8

"""
    Lists

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.lists.api_client import ApiClient
from hubspot.crm.lists.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class MappingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def translate_legacy_list_id_to_list_id(self, **kwargs):  # noqa: E501
        """Translate Legacy List Id to Modern List Id  # noqa: E501

        This API allows translation of legacy list id to list id. This is a temporary API allowed for mapping old id's to new id's and will expire on May 30th, 2025.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.translate_legacy_list_id_to_list_id(async_req=True)
        >>> result = thread.get()

        :param legacy_list_id: The legacy list id from lists v1 API.
        :type legacy_list_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PublicMigrationMapping
        """
        kwargs["_return_http_data_only"] = True
        return self.translate_legacy_list_id_to_list_id_with_http_info(**kwargs)  # noqa: E501

    def translate_legacy_list_id_to_list_id_with_http_info(self, **kwargs):  # noqa: E501
        """Translate Legacy List Id to Modern List Id  # noqa: E501

        This API allows translation of legacy list id to list id. This is a temporary API allowed for mapping old id's to new id's and will expire on May 30th, 2025.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.translate_legacy_list_id_to_list_id_with_http_info(async_req=True)
        >>> result = thread.get()

        :param legacy_list_id: The legacy list id from lists v1 API.
        :type legacy_list_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PublicMigrationMapping, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["legacy_list_id"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method translate_legacy_list_id_to_list_id" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get("legacy_list_id") is not None:  # noqa: E501
            query_params.append(("legacyListId", local_var_params["legacy_list_id"]))  # noqa: E501

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "PublicMigrationMapping",
        }

        return self.api_client.call_api(
            "/crm/v3/lists/idmapping",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )

    def translate_legacy_list_id_to_list_id_batch(self, request_body, **kwargs):  # noqa: E501
        """Translate Legacy List Id to Modern List Id in Batch  # noqa: E501

        This API allows translation of a batch of legacy list id's to list id's. This allows for a maximum of 10,000 id's. This is a temporary API allowed for mapping old id's to new id's and will expire on May 30th, 2025.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.translate_legacy_list_id_to_list_id_batch(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PublicBatchMigrationMapping
        """
        kwargs["_return_http_data_only"] = True
        return self.translate_legacy_list_id_to_list_id_batch_with_http_info(request_body, **kwargs)  # noqa: E501

    def translate_legacy_list_id_to_list_id_batch_with_http_info(self, request_body, **kwargs):  # noqa: E501
        """Translate Legacy List Id to Modern List Id in Batch  # noqa: E501

        This API allows translation of a batch of legacy list id's to list id's. This allows for a maximum of 10,000 id's. This is a temporary API allowed for mapping old id's to new id's and will expire on May 30th, 2025.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.translate_legacy_list_id_to_list_id_batch_with_http_info(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PublicBatchMigrationMapping, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["request_body"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method translate_legacy_list_id_to_list_id_batch" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'request_body' is set
        if self.api_client.client_side_validation and local_var_params.get("request_body") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `request_body` when calling `translate_legacy_list_id_to_list_id_batch`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "request_body" in local_var_params:
            body_params = local_var_params["request_body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "PublicBatchMigrationMapping",
        }

        return self.api_client.call_api(
            "/crm/v3/lists/idmapping",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )
