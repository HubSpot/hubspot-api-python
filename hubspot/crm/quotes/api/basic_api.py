"""
    Quotes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""



import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.quotes.api_client import ApiClient
from hubspot.crm.quotes.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class BasicApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_by_id(self, quote_id, **kwargs):  # noqa: E501
        """Read  # noqa: E501

        Read an Object identified by `{quoteId}`. `{quoteId}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param.  Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id(quote_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str quote_id: (required)
        :param list[str] properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :param bool paginate_associations:
        :param bool archived: Whether to return only results that have been archived.
        :param str id_property: The name of a property whose values are unique for this object type
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SimplePublicObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_by_id_with_http_info(quote_id, **kwargs)  # noqa: E501

    def get_by_id_with_http_info(self, quote_id, **kwargs):  # noqa: E501
        """Read  # noqa: E501

        Read an Object identified by `{quoteId}`. `{quoteId}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param.  Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_with_http_info(quote_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str quote_id: (required)
        :param list[str] properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :param bool paginate_associations:
        :param bool archived: Whether to return only results that have been archived.
        :param str id_property: The name of a property whose values are unique for this object type
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SimplePublicObject, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "quote_id",
            "properties",
            "associations",
            "paginate_associations",
            "archived",
            "id_property",
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
                    " to method get_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'quote_id' is set
        if self.api_client.client_side_validation and (
            "quote_id" not in local_var_params
            or local_var_params["quote_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `quote_id` when calling `get_by_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "quote_id" in local_var_params:
            path_params["quoteId"] = local_var_params["quote_id"]  # noqa: E501

        query_params = []
        if (
            "properties" in local_var_params
            and local_var_params["properties"] is not None
        ):  # noqa: E501
            query_params.append(
                ("properties", local_var_params["properties"])
            )  # noqa: E501
            collection_formats["properties"] = "multi"  # noqa: E501
        if (
            "associations" in local_var_params
            and local_var_params["associations"] is not None
        ):  # noqa: E501
            query_params.append(
                ("associations", local_var_params["associations"])
            )  # noqa: E501
            collection_formats["associations"] = "multi"  # noqa: E501
        if (
            "paginate_associations" in local_var_params
            and local_var_params["paginate_associations"] is not None
        ):  # noqa: E501
            query_params.append(
                ("paginateAssociations", local_var_params["paginate_associations"])
            )  # noqa: E501
        if (
            "archived" in local_var_params and local_var_params["archived"] is not None
        ):  # noqa: E501
            query_params.append(
                ("archived", local_var_params["archived"])
            )  # noqa: E501
        if (
            "id_property" in local_var_params
            and local_var_params["id_property"] is not None
        ):  # noqa: E501
            query_params.append(
                ("idProperty", local_var_params["id_property"])
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
        auth_settings = ["hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/objects/quotes/{quoteId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="SimplePublicObject",  # noqa: E501
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
        """List  # noqa: E501

        Read a page of quotes. Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: The maximum number of results to display per page.
        :param str after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :param list[str] properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :param bool paginate_associations:
        :param bool archived: Whether to return only results that have been archived.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CollectionResponseSimplePublicObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_page_with_http_info(**kwargs)  # noqa: E501

    def get_page_with_http_info(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        Read a page of quotes. Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: The maximum number of results to display per page.
        :param str after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :param list[str] properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :param bool paginate_associations:
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
        :return: tuple(CollectionResponseSimplePublicObject, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "limit",
            "after",
            "properties",
            "associations",
            "paginate_associations",
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
            "limit" in local_var_params and local_var_params["limit"] is not None
        ):  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501
        if (
            "after" in local_var_params and local_var_params["after"] is not None
        ):  # noqa: E501
            query_params.append(("after", local_var_params["after"]))  # noqa: E501
        if (
            "properties" in local_var_params
            and local_var_params["properties"] is not None
        ):  # noqa: E501
            query_params.append(
                ("properties", local_var_params["properties"])
            )  # noqa: E501
            collection_formats["properties"] = "multi"  # noqa: E501
        if (
            "associations" in local_var_params
            and local_var_params["associations"] is not None
        ):  # noqa: E501
            query_params.append(
                ("associations", local_var_params["associations"])
            )  # noqa: E501
            collection_formats["associations"] = "multi"  # noqa: E501
        if (
            "paginate_associations" in local_var_params
            and local_var_params["paginate_associations"] is not None
        ):  # noqa: E501
            query_params.append(
                ("paginateAssociations", local_var_params["paginate_associations"])
            )  # noqa: E501
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
        auth_settings = ["hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/objects/quotes",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CollectionResponseSimplePublicObject",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
