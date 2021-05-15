"""
    CMS Site Search

    Use these endpoints for searching content on your HubSpot hosted CMS website(s).  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""



import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.cms.site_search.api_client import ApiClient
from hubspot.cms.site_search.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class DefaultApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_by_id(self, content_id, **kwargs):  # noqa: E501
        """Get indexed properties.  # noqa: E501

        For a given account and document ID (page ID, blog post ID, HubDB row ID, etc.), return all indexed data for that document. This is useful when debugging why a particular document is not returned from a custom search.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id(content_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str content_id: ID of the target document when searching for indexed properties. (required)
        :param str type: The type of document. Can be one of `SITE_PAGE`, `BLOG_POST`, or `KNOWLEDGE_ARTICLE`.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: IndexedData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_by_id_with_http_info(content_id, **kwargs)  # noqa: E501

    def get_by_id_with_http_info(self, content_id, **kwargs):  # noqa: E501
        """Get indexed properties.  # noqa: E501

        For a given account and document ID (page ID, blog post ID, HubDB row ID, etc.), return all indexed data for that document. This is useful when debugging why a particular document is not returned from a custom search.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_with_http_info(content_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str content_id: ID of the target document when searching for indexed properties. (required)
        :param str type: The type of document. Can be one of `SITE_PAGE`, `BLOG_POST`, or `KNOWLEDGE_ARTICLE`.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(IndexedData, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["content_id", "type"]
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
        # verify the required parameter 'content_id' is set
        if self.api_client.client_side_validation and (
            "content_id" not in local_var_params
            or local_var_params["content_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `content_id` when calling `get_by_id`"
            )  # noqa: E501

        if (
            self.api_client.client_side_validation
            and "content_id" in local_var_params
            and not re.search(r".*", local_var_params["content_id"])
        ):  # noqa: E501
            raise ApiValueError(
                "Invalid value for parameter `content_id` when calling `get_by_id`, must conform to the pattern `/.*/`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}
        if "content_id" in local_var_params:
            path_params["contentId"] = local_var_params["content_id"]  # noqa: E501

        query_params = []
        if (
            "type" in local_var_params and local_var_params["type"] is not None
        ):  # noqa: E501
            query_params.append(("type", local_var_params["type"]))  # noqa: E501

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
            "/cms/v3/site-search/indexed-data/{contentId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="IndexedData",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def search(self, **kwargs):  # noqa: E501
        """Search your site.  # noqa: E501

        Returns any website content matching the given search criteria for a given HubSpot account. Searches can be filtered by content type, domain, or URL path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str q: The term to search for.
        :param int limit: Specifies the number of results to be returned in a single response. Defaults to `10`. Maximum value is `100`.
        :param int offset: Used to page through the results. If there are more results than specified by the `limit` parameter, you will need to use the value of offset returned in the previous request to get the next set of results.
        :param str language: Specifies the language of content to be searched. This value must be a valid [ISO 639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `es` for Spanish)
        :param bool match_prefix: Inverts the behavior of the pathPrefix filter when set to `false`. Defaults to `true`.
        :param bool autocomplete: Specifies whether or not you are showing autocomplete results. Defaults to false.
        :param float popularity_boost: Specifies how strongly a result is boosted based on its view count. Defaults to 1.0.
        :param float boost_limit: Specifies the maximum amount a result will be boosted based on its view count. Defaults to 5.0. Read more about elasticsearch boosting [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-boost.html).
        :param float min_score: Specifies the minimum search score threshold for returned results. This value is intentionally set low by default in order to return many results. Increase this for higher precision, but less recall.
        :param str boost_recent: Specifies a relative time window where scores of documents published outside this time window decay. This can only be used for blog posts. For example, boostRecent=10d will boost documents published within the last 10 days. Supported timeunits are ms (milliseconds), s (seconds), m (minutes), h (hours), d (days).
        :param int table_id: Specifies a specific HubDB table to search. Only returns results from the specified table. Can be used in tandem with the `hubdbQuery` parameter to further filter results.
        :param str hubdb_query: Specify a HubDB query to further filter the search results.
        :param str key_string:
        :param list[str] domain: A domain to match search results for. Multiple domains can be provided with &.
        :param list[str] type: Specifies the type of content to search. Can be one or more of SITE_PAGE, LANDING_PAGE, BLOG_POST, LISTING_PAGE, and KNOWLEDGE_ARTICLE. Defaults to all content types except LANDING_PAGE and KNOWLEDGE_ARTICLE
        :param list[str] path_prefix: Specifies a path prefix to filter search results. Will only return results with URL paths that start with the specified parameter. Can be used multiple times.
        :param list[str] _property: Specifies which properties to include in the search. Options include `title`, `description`, and `html`. All properties will be searched by default.
        :param str length: Specifies the length of the search results. Can be set to `LONG` or `SHORT`. `SHORT` will return the first 128 characters of the content's meta description. `LONG` will build a more detailed content snippet based on the html/content of the page.
        :param list[int] group_id: Specifies which blog(s) to be searched by blog ID. Can be used multiple times to search more than one blog.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PublicSearchResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.search_with_http_info(**kwargs)  # noqa: E501

    def search_with_http_info(self, **kwargs):  # noqa: E501
        """Search your site.  # noqa: E501

        Returns any website content matching the given search criteria for a given HubSpot account. Searches can be filtered by content type, domain, or URL path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str q: The term to search for.
        :param int limit: Specifies the number of results to be returned in a single response. Defaults to `10`. Maximum value is `100`.
        :param int offset: Used to page through the results. If there are more results than specified by the `limit` parameter, you will need to use the value of offset returned in the previous request to get the next set of results.
        :param str language: Specifies the language of content to be searched. This value must be a valid [ISO 639-1 language code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `es` for Spanish)
        :param bool match_prefix: Inverts the behavior of the pathPrefix filter when set to `false`. Defaults to `true`.
        :param bool autocomplete: Specifies whether or not you are showing autocomplete results. Defaults to false.
        :param float popularity_boost: Specifies how strongly a result is boosted based on its view count. Defaults to 1.0.
        :param float boost_limit: Specifies the maximum amount a result will be boosted based on its view count. Defaults to 5.0. Read more about elasticsearch boosting [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-boost.html).
        :param float min_score: Specifies the minimum search score threshold for returned results. This value is intentionally set low by default in order to return many results. Increase this for higher precision, but less recall.
        :param str boost_recent: Specifies a relative time window where scores of documents published outside this time window decay. This can only be used for blog posts. For example, boostRecent=10d will boost documents published within the last 10 days. Supported timeunits are ms (milliseconds), s (seconds), m (minutes), h (hours), d (days).
        :param int table_id: Specifies a specific HubDB table to search. Only returns results from the specified table. Can be used in tandem with the `hubdbQuery` parameter to further filter results.
        :param str hubdb_query: Specify a HubDB query to further filter the search results.
        :param str key_string:
        :param list[str] domain: A domain to match search results for. Multiple domains can be provided with &.
        :param list[str] type: Specifies the type of content to search. Can be one or more of SITE_PAGE, LANDING_PAGE, BLOG_POST, LISTING_PAGE, and KNOWLEDGE_ARTICLE. Defaults to all content types except LANDING_PAGE and KNOWLEDGE_ARTICLE
        :param list[str] path_prefix: Specifies a path prefix to filter search results. Will only return results with URL paths that start with the specified parameter. Can be used multiple times.
        :param list[str] _property: Specifies which properties to include in the search. Options include `title`, `description`, and `html`. All properties will be searched by default.
        :param str length: Specifies the length of the search results. Can be set to `LONG` or `SHORT`. `SHORT` will return the first 128 characters of the content's meta description. `LONG` will build a more detailed content snippet based on the html/content of the page.
        :param list[int] group_id: Specifies which blog(s) to be searched by blog ID. Can be used multiple times to search more than one blog.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PublicSearchResults, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "q",
            "limit",
            "offset",
            "language",
            "match_prefix",
            "autocomplete",
            "popularity_boost",
            "boost_limit",
            "min_score",
            "boost_recent",
            "table_id",
            "hubdb_query",
            "key_string",
            "domain",
            "type",
            "path_prefix",
            "_property",
            "length",
            "group_id",
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
                    "Got an unexpected keyword argument '%s'" " to method search" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "q" in local_var_params and local_var_params["q"] is not None:  # noqa: E501
            query_params.append(("q", local_var_params["q"]))  # noqa: E501
        if (
            "limit" in local_var_params and local_var_params["limit"] is not None
        ):  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501
        if (
            "offset" in local_var_params and local_var_params["offset"] is not None
        ):  # noqa: E501
            query_params.append(("offset", local_var_params["offset"]))  # noqa: E501
        if (
            "language" in local_var_params and local_var_params["language"] is not None
        ):  # noqa: E501
            query_params.append(
                ("language", local_var_params["language"])
            )  # noqa: E501
        if (
            "match_prefix" in local_var_params
            and local_var_params["match_prefix"] is not None
        ):  # noqa: E501
            query_params.append(
                ("matchPrefix", local_var_params["match_prefix"])
            )  # noqa: E501
        if (
            "autocomplete" in local_var_params
            and local_var_params["autocomplete"] is not None
        ):  # noqa: E501
            query_params.append(
                ("autocomplete", local_var_params["autocomplete"])
            )  # noqa: E501
        if (
            "popularity_boost" in local_var_params
            and local_var_params["popularity_boost"] is not None
        ):  # noqa: E501
            query_params.append(
                ("popularityBoost", local_var_params["popularity_boost"])
            )  # noqa: E501
        if (
            "boost_limit" in local_var_params
            and local_var_params["boost_limit"] is not None
        ):  # noqa: E501
            query_params.append(
                ("boostLimit", local_var_params["boost_limit"])
            )  # noqa: E501
        if (
            "min_score" in local_var_params
            and local_var_params["min_score"] is not None
        ):  # noqa: E501
            query_params.append(
                ("minScore", local_var_params["min_score"])
            )  # noqa: E501
        if (
            "boost_recent" in local_var_params
            and local_var_params["boost_recent"] is not None
        ):  # noqa: E501
            query_params.append(
                ("boostRecent", local_var_params["boost_recent"])
            )  # noqa: E501
        if (
            "table_id" in local_var_params and local_var_params["table_id"] is not None
        ):  # noqa: E501
            query_params.append(("tableId", local_var_params["table_id"]))  # noqa: E501
        if (
            "hubdb_query" in local_var_params
            and local_var_params["hubdb_query"] is not None
        ):  # noqa: E501
            query_params.append(
                ("hubdbQuery", local_var_params["hubdb_query"])
            )  # noqa: E501
        if (
            "key_string" in local_var_params
            and local_var_params["key_string"] is not None
        ):  # noqa: E501
            query_params.append(
                ("keyString", local_var_params["key_string"])
            )  # noqa: E501
        if (
            "domain" in local_var_params and local_var_params["domain"] is not None
        ):  # noqa: E501
            query_params.append(("domain", local_var_params["domain"]))  # noqa: E501
            collection_formats["domain"] = "multi"  # noqa: E501
        if (
            "type" in local_var_params and local_var_params["type"] is not None
        ):  # noqa: E501
            query_params.append(("type", local_var_params["type"]))  # noqa: E501
            collection_formats["type"] = "multi"  # noqa: E501
        if (
            "path_prefix" in local_var_params
            and local_var_params["path_prefix"] is not None
        ):  # noqa: E501
            query_params.append(
                ("pathPrefix", local_var_params["path_prefix"])
            )  # noqa: E501
            collection_formats["pathPrefix"] = "multi"  # noqa: E501
        if (
            "_property" in local_var_params
            and local_var_params["_property"] is not None
        ):  # noqa: E501
            query_params.append(
                ("property", local_var_params["_property"])
            )  # noqa: E501
            collection_formats["property"] = "multi"  # noqa: E501
        if (
            "length" in local_var_params and local_var_params["length"] is not None
        ):  # noqa: E501
            query_params.append(("length", local_var_params["length"]))  # noqa: E501
        if (
            "group_id" in local_var_params and local_var_params["group_id"] is not None
        ):  # noqa: E501
            query_params.append(("groupId", local_var_params["group_id"]))  # noqa: E501
            collection_formats["groupId"] = "multi"  # noqa: E501

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
            "/cms/v3/site-search/search",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PublicSearchResults",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
