"""
    URL redirects

    URL redirect operations  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""



import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.cms.url_redirects.api_client import ApiClient
from hubspot.cms.url_redirects.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError,
)


class RedirectsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, url_redirect_id, **kwargs):  # noqa: E501
        """Delete a redirect  # noqa: E501

        Delete one existing redirect, so it is no longer mapped.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive(url_redirect_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str url_redirect_id: The ID of the target redirect. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.archive_with_http_info(url_redirect_id, **kwargs)  # noqa: E501

    def archive_with_http_info(self, url_redirect_id, **kwargs):  # noqa: E501
        """Delete a redirect  # noqa: E501

        Delete one existing redirect, so it is no longer mapped.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_with_http_info(url_redirect_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str url_redirect_id: The ID of the target redirect. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["url_redirect_id"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in local_var_params["kwargs"].items():
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method archive" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'url_redirect_id' is set
        if self.api_client.client_side_validation and (
            "url_redirect_id" not in local_var_params
            or local_var_params["url_redirect_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `url_redirect_id` when calling `archive`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "url_redirect_id" in local_var_params:
            path_params["urlRedirectId"] = local_var_params[
                "url_redirect_id"
            ]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["*/*"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/cms/v3/url-redirects/{urlRedirectId}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create(self, **kwargs):  # noqa: E501
        """Create a redirect  # noqa: E501

        Creates and configures a new URL redirect.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param UrlMappingCreateRequestBody url_mapping_create_request_body:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UrlMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_with_http_info(**kwargs)  # noqa: E501

    def create_with_http_info(self, **kwargs):  # noqa: E501
        """Create a redirect  # noqa: E501

        Creates and configures a new URL redirect.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param UrlMappingCreateRequestBody url_mapping_create_request_body:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UrlMapping, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["url_mapping_create_request_body"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in local_var_params["kwargs"].items():
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "url_mapping_create_request_body" in local_var_params:
            body_params = local_var_params["url_mapping_create_request_body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/cms/v3/url-redirects/",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="UrlMapping",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_by_id(self, url_redirect_id, **kwargs):  # noqa: E501
        """Get details for a redirect  # noqa: E501

        Returns the details for a single existing URL redirect by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id(url_redirect_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str url_redirect_id: The ID of the target redirect. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UrlMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_by_id_with_http_info(url_redirect_id, **kwargs)  # noqa: E501

    def get_by_id_with_http_info(self, url_redirect_id, **kwargs):  # noqa: E501
        """Get details for a redirect  # noqa: E501

        Returns the details for a single existing URL redirect by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_with_http_info(url_redirect_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str url_redirect_id: The ID of the target redirect. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UrlMapping, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["url_redirect_id"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in local_var_params["kwargs"].items():
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'url_redirect_id' is set
        if self.api_client.client_side_validation and (
            "url_redirect_id" not in local_var_params
            or local_var_params["url_redirect_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `url_redirect_id` when calling `get_by_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "url_redirect_id" in local_var_params:
            path_params["urlRedirectId"] = local_var_params[
                "url_redirect_id"
            ]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/cms/v3/url-redirects/{urlRedirectId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="UrlMapping",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_page(self, **kwargs):  # noqa: E501
        """Get current redirects  # noqa: E501

        Returns all existing URL redirects. Results can be limited and filtered by creation or updated date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param datetime created_at: Only return redirects created on exactly this date.
        :param datetime created_after: Only return redirects created after this date.
        :param datetime created_before: Only return redirects created before this date.
        :param datetime updated_at: Only return redirects last updated on exactly this date.
        :param datetime updated_after: Only return redirects last updated after this date.
        :param datetime updated_before: Only return redirects last updated before this date.
        :param list[str] sort:
        :param list[str] properties:
        :param str after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :param str before:
        :param int limit: Maximum number of result per page
        :param bool archived: Whether to return only results that have been archived.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CollectionResponseWithTotalUrlMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_page_with_http_info(**kwargs)  # noqa: E501

    def get_page_with_http_info(self, **kwargs):  # noqa: E501
        """Get current redirects  # noqa: E501

        Returns all existing URL redirects. Results can be limited and filtered by creation or updated date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param datetime created_at: Only return redirects created on exactly this date.
        :param datetime created_after: Only return redirects created after this date.
        :param datetime created_before: Only return redirects created before this date.
        :param datetime updated_at: Only return redirects last updated on exactly this date.
        :param datetime updated_after: Only return redirects last updated after this date.
        :param datetime updated_before: Only return redirects last updated before this date.
        :param list[str] sort:
        :param list[str] properties:
        :param str after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :param str before:
        :param int limit: Maximum number of result per page
        :param bool archived: Whether to return only results that have been archived.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CollectionResponseWithTotalUrlMapping, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "created_at",
            "created_after",
            "created_before",
            "updated_at",
            "updated_after",
            "updated_before",
            "sort",
            "properties",
            "after",
            "before",
            "limit",
            "archived",
        ]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in local_var_params["kwargs"].items():
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_page" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if (
            "created_at" in local_var_params
            and local_var_params["created_at"] is not None
        ):  # noqa: E501
            query_params.append(
                ("createdAt", local_var_params["created_at"])
            )  # noqa: E501
        if (
            "created_after" in local_var_params
            and local_var_params["created_after"] is not None
        ):  # noqa: E501
            query_params.append(
                ("createdAfter", local_var_params["created_after"])
            )  # noqa: E501
        if (
            "created_before" in local_var_params
            and local_var_params["created_before"] is not None
        ):  # noqa: E501
            query_params.append(
                ("createdBefore", local_var_params["created_before"])
            )  # noqa: E501
        if (
            "updated_at" in local_var_params
            and local_var_params["updated_at"] is not None
        ):  # noqa: E501
            query_params.append(
                ("updatedAt", local_var_params["updated_at"])
            )  # noqa: E501
        if (
            "updated_after" in local_var_params
            and local_var_params["updated_after"] is not None
        ):  # noqa: E501
            query_params.append(
                ("updatedAfter", local_var_params["updated_after"])
            )  # noqa: E501
        if (
            "updated_before" in local_var_params
            and local_var_params["updated_before"] is not None
        ):  # noqa: E501
            query_params.append(
                ("updatedBefore", local_var_params["updated_before"])
            )  # noqa: E501
        if (
            "sort" in local_var_params and local_var_params["sort"] is not None
        ):  # noqa: E501
            query_params.append(("sort", local_var_params["sort"]))  # noqa: E501
            collection_formats["sort"] = "multi"  # noqa: E501
        if (
            "properties" in local_var_params
            and local_var_params["properties"] is not None
        ):  # noqa: E501
            query_params.append(
                ("properties", local_var_params["properties"])
            )  # noqa: E501
            collection_formats["properties"] = "multi"  # noqa: E501
        if (
            "after" in local_var_params and local_var_params["after"] is not None
        ):  # noqa: E501
            query_params.append(("after", local_var_params["after"]))  # noqa: E501
        if (
            "before" in local_var_params and local_var_params["before"] is not None
        ):  # noqa: E501
            query_params.append(("before", local_var_params["before"]))  # noqa: E501
        if (
            "limit" in local_var_params and local_var_params["limit"] is not None
        ):  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501
        if (
            "archived" in local_var_params and local_var_params["archived"] is not None
        ):  # noqa: E501
            query_params.append(
                ("archived", local_var_params["archived"])
            )  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/cms/v3/url-redirects/",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CollectionResponseWithTotalUrlMapping",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update(self, url_redirect_id, **kwargs):  # noqa: E501
        """Update a redirect  # noqa: E501

        Updates the settings for an existing URL redirect.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(url_redirect_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str url_redirect_id: (required)
        :param UrlMapping url_mapping:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UrlMapping
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.update_with_http_info(url_redirect_id, **kwargs)  # noqa: E501

    def update_with_http_info(self, url_redirect_id, **kwargs):  # noqa: E501
        """Update a redirect  # noqa: E501

        Updates the settings for an existing URL redirect.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(url_redirect_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str url_redirect_id: (required)
        :param UrlMapping url_mapping:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UrlMapping, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["url_redirect_id", "url_mapping"]
        all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
            ]
        )

        for key, val in local_var_params["kwargs"].items():
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method update" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'url_redirect_id' is set
        if self.api_client.client_side_validation and (
            "url_redirect_id" not in local_var_params
            or local_var_params["url_redirect_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `url_redirect_id` when calling `update`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "url_redirect_id" in local_var_params:
            path_params["urlRedirectId"] = local_var_params[
                "url_redirect_id"
            ]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "url_mapping" in local_var_params:
            body_params = local_var_params["url_mapping"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "*/*"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            "Content-Type"
        ] = self.api_client.select_header_content_type(  # noqa: E501
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        return self.api_client.call_api(
            "/cms/v3/url-redirects/{urlRedirectId}",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="UrlMapping",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
