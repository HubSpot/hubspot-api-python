# coding: utf-8

"""
    Cms Content Audit

    Use this endpoint to query audit logs of CMS changes that occurred on your HubSpot account.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.cms.audit_logs.api_client import ApiClient
from hubspot.cms.audit_logs.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class AuditLogsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_page(self, **kwargs):  # noqa: E501
        """Query audit logs  # noqa: E501

        Returns audit logs based on filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_page(async_req=True)
        >>> result = thread.get()

        :param user_id: Comma separated list of user ids to filter by.
        :type user_id: list[str]
        :param event_type: Comma separated list of event types to filter by (CREATED, UPDATED, PUBLISHED, DELETED, UNPUBLISHED).
        :type event_type: list[str]
        :param object_type: Comma separated list of object types to filter by (BLOG, LANDING_PAGE, DOMAIN, HUBDB_TABLE etc.)
        :type object_type: list[str]
        :param object_id: Comma separated list of object ids to filter by.
        :type object_id: list[str]
        :param after: Timestamp after which audit logs will be returned
        :type after: str
        :param before: Timestamp before which audit logs will be returned
        :type before: str
        :param limit: The number of logs to return.
        :type limit: int
        :param sort: The sort direction for the audit logs. (Can only sort by timestamp).
        :type sort: list[str]
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
        :rtype: CollectionResponsePublicAuditLog
        """
        kwargs["_return_http_data_only"] = True
        return self.get_page_with_http_info(**kwargs)  # noqa: E501

    def get_page_with_http_info(self, **kwargs):  # noqa: E501
        """Query audit logs  # noqa: E501

        Returns audit logs based on filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_page_with_http_info(async_req=True)
        >>> result = thread.get()

        :param user_id: Comma separated list of user ids to filter by.
        :type user_id: list[str]
        :param event_type: Comma separated list of event types to filter by (CREATED, UPDATED, PUBLISHED, DELETED, UNPUBLISHED).
        :type event_type: list[str]
        :param object_type: Comma separated list of object types to filter by (BLOG, LANDING_PAGE, DOMAIN, HUBDB_TABLE etc.)
        :type object_type: list[str]
        :param object_id: Comma separated list of object ids to filter by.
        :type object_id: list[str]
        :param after: Timestamp after which audit logs will be returned
        :type after: str
        :param before: Timestamp before which audit logs will be returned
        :type before: str
        :param limit: The number of logs to return.
        :type limit: int
        :param sort: The sort direction for the audit logs. (Can only sort by timestamp).
        :type sort: list[str]
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
        :rtype: tuple(CollectionResponsePublicAuditLog, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["user_id", "event_type", "object_type", "object_id", "after", "before", "limit", "sort"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_page" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get("user_id") is not None:  # noqa: E501
            query_params.append(("userId", local_var_params["user_id"]))  # noqa: E501
            collection_formats["userId"] = "multi"  # noqa: E501
        if local_var_params.get("event_type") is not None:  # noqa: E501
            query_params.append(("eventType", local_var_params["event_type"]))  # noqa: E501
            collection_formats["eventType"] = "multi"  # noqa: E501
        if local_var_params.get("object_type") is not None:  # noqa: E501
            query_params.append(("objectType", local_var_params["object_type"]))  # noqa: E501
            collection_formats["objectType"] = "multi"  # noqa: E501
        if local_var_params.get("object_id") is not None:  # noqa: E501
            query_params.append(("objectId", local_var_params["object_id"]))  # noqa: E501
            collection_formats["objectId"] = "multi"  # noqa: E501
        if local_var_params.get("after") is not None:  # noqa: E501
            query_params.append(("after", local_var_params["after"]))  # noqa: E501
        if local_var_params.get("before") is not None:  # noqa: E501
            query_params.append(("before", local_var_params["before"]))  # noqa: E501
        if local_var_params.get("limit") is not None:  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501
        if local_var_params.get("sort") is not None:  # noqa: E501
            query_params.append(("sort", local_var_params["sort"]))  # noqa: E501
            collection_formats["sort"] = "multi"  # noqa: E501

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "CollectionResponsePublicAuditLog",
        }

        return self.api_client.call_api(
            "/cms/v3/audit-logs/",
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
