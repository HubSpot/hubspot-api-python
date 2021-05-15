"""
    CMS Performance API

    Use these endpoints to get a time series view of your website's performance.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""



import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.cms.performance.api_client import ApiClient
from hubspot.cms.performance.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class DefaultApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_page(self, **kwargs):  # noqa: E501
        """View your website's performance.  # noqa: E501

        Returns time series data website performance data for the given domain and/or path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str domain: The domain to search return data for.
        :param str path: The url path of the domain to return data for.
        :param bool pad: Specifies whether the time series data should have empty intervals if performance data is not present to create a continuous set.
        :param bool sum: Specifies whether the time series data should be summated for the given period. Defaults to false.
        :param str period: A relative period to return time series data for. This value is ignored if start and/or end are provided. Valid periods: [15m, 30m, 1h, 4h, 12h, 1d, 1w]
        :param str interval: The time series interval to group data by. Valid intervals: [1m, 5m, 15m, 30m, 1h, 4h, 12h, 1d, 1w]
        :param int start: A timestamp in milliseconds that indicates the start of the time period.
        :param int end: A timestamp in milliseconds that indicates the end of the time period.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PublicPerformanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_page_with_http_info(**kwargs)  # noqa: E501

    def get_page_with_http_info(self, **kwargs):  # noqa: E501
        """View your website's performance.  # noqa: E501

        Returns time series data website performance data for the given domain and/or path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_page_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str domain: The domain to search return data for.
        :param str path: The url path of the domain to return data for.
        :param bool pad: Specifies whether the time series data should have empty intervals if performance data is not present to create a continuous set.
        :param bool sum: Specifies whether the time series data should be summated for the given period. Defaults to false.
        :param str period: A relative period to return time series data for. This value is ignored if start and/or end are provided. Valid periods: [15m, 30m, 1h, 4h, 12h, 1d, 1w]
        :param str interval: The time series interval to group data by. Valid intervals: [1m, 5m, 15m, 30m, 1h, 4h, 12h, 1d, 1w]
        :param int start: A timestamp in milliseconds that indicates the start of the time period.
        :param int end: A timestamp in milliseconds that indicates the end of the time period.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PublicPerformanceResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "domain",
            "path",
            "pad",
            "sum",
            "period",
            "interval",
            "start",
            "end",
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
            "domain" in local_var_params and local_var_params["domain"] is not None
        ):  # noqa: E501
            query_params.append(("domain", local_var_params["domain"]))  # noqa: E501
        if (
            "path" in local_var_params and local_var_params["path"] is not None
        ):  # noqa: E501
            query_params.append(("path", local_var_params["path"]))  # noqa: E501
        if (
            "pad" in local_var_params and local_var_params["pad"] is not None
        ):  # noqa: E501
            query_params.append(("pad", local_var_params["pad"]))  # noqa: E501
        if (
            "sum" in local_var_params and local_var_params["sum"] is not None
        ):  # noqa: E501
            query_params.append(("sum", local_var_params["sum"]))  # noqa: E501
        if (
            "period" in local_var_params and local_var_params["period"] is not None
        ):  # noqa: E501
            query_params.append(("period", local_var_params["period"]))  # noqa: E501
        if (
            "interval" in local_var_params and local_var_params["interval"] is not None
        ):  # noqa: E501
            query_params.append(
                ("interval", local_var_params["interval"])
            )  # noqa: E501
        if (
            "start" in local_var_params and local_var_params["start"] is not None
        ):  # noqa: E501
            query_params.append(("start", local_var_params["start"]))  # noqa: E501
        if (
            "end" in local_var_params and local_var_params["end"] is not None
        ):  # noqa: E501
            query_params.append(("end", local_var_params["end"]))  # noqa: E501

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
            "/cms/v3/performance/",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PublicPerformanceResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_uptime(self, **kwargs):  # noqa: E501
        """View your website's uptime.  # noqa: E501

        Returns uptime time series website performance data for the given domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_uptime(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str domain: The domain to search return data for.
        :param str path:
        :param bool pad: Specifies whether the time series data should have empty intervals if performance data is not present to create a continuous set.
        :param bool sum: Specifies whether the time series data should be summated for the given period. Defaults to false.
        :param str period: A relative period to return time series data for. This value is ignored if start and/or end are provided. Valid periods: [15m, 30m, 1h, 4h, 12h, 1d, 1w]
        :param str interval: The time series interval to group data by. Valid intervals: [1m, 5m, 15m, 30m, 1h, 4h, 12h, 1d, 1w]
        :param int start: A timestamp in milliseconds that indicates the start of the time period.
        :param int end: A timestamp in milliseconds that indicates the end of the time period.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PublicPerformanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.get_uptime_with_http_info(**kwargs)  # noqa: E501

    def get_uptime_with_http_info(self, **kwargs):  # noqa: E501
        """View your website's uptime.  # noqa: E501

        Returns uptime time series website performance data for the given domain.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_uptime_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str domain: The domain to search return data for.
        :param str path:
        :param bool pad: Specifies whether the time series data should have empty intervals if performance data is not present to create a continuous set.
        :param bool sum: Specifies whether the time series data should be summated for the given period. Defaults to false.
        :param str period: A relative period to return time series data for. This value is ignored if start and/or end are provided. Valid periods: [15m, 30m, 1h, 4h, 12h, 1d, 1w]
        :param str interval: The time series interval to group data by. Valid intervals: [1m, 5m, 15m, 30m, 1h, 4h, 12h, 1d, 1w]
        :param int start: A timestamp in milliseconds that indicates the start of the time period.
        :param int end: A timestamp in milliseconds that indicates the end of the time period.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PublicPerformanceResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "domain",
            "path",
            "pad",
            "sum",
            "period",
            "interval",
            "start",
            "end",
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
                    " to method get_uptime" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if (
            "domain" in local_var_params and local_var_params["domain"] is not None
        ):  # noqa: E501
            query_params.append(("domain", local_var_params["domain"]))  # noqa: E501
        if (
            "path" in local_var_params and local_var_params["path"] is not None
        ):  # noqa: E501
            query_params.append(("path", local_var_params["path"]))  # noqa: E501
        if (
            "pad" in local_var_params and local_var_params["pad"] is not None
        ):  # noqa: E501
            query_params.append(("pad", local_var_params["pad"]))  # noqa: E501
        if (
            "sum" in local_var_params and local_var_params["sum"] is not None
        ):  # noqa: E501
            query_params.append(("sum", local_var_params["sum"]))  # noqa: E501
        if (
            "period" in local_var_params and local_var_params["period"] is not None
        ):  # noqa: E501
            query_params.append(("period", local_var_params["period"]))  # noqa: E501
        if (
            "interval" in local_var_params and local_var_params["interval"] is not None
        ):  # noqa: E501
            query_params.append(
                ("interval", local_var_params["interval"])
            )  # noqa: E501
        if (
            "start" in local_var_params and local_var_params["start"] is not None
        ):  # noqa: E501
            query_params.append(("start", local_var_params["start"]))  # noqa: E501
        if (
            "end" in local_var_params and local_var_params["end"] is not None
        ):  # noqa: E501
            query_params.append(("end", local_var_params["end"]))  # noqa: E501

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
            "/cms/v3/performance/uptime",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PublicPerformanceResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
