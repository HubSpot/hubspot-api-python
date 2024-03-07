# coding: utf-8

"""
    Transactional Single Send

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.marketing.transactional.api_client import ApiClient
from hubspot.marketing.transactional.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class SingleSendApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def send_email(self, public_single_send_request_egg, **kwargs):  # noqa: E501
        """Send a single transactional email asynchronously.  # noqa: E501

        Asynchronously send a transactional email. Returns the status of the email send with a statusId that can be used to continuously query for the status using the Email Send Status API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_email(public_single_send_request_egg, async_req=True)
        >>> result = thread.get()

        :param public_single_send_request_egg: A request object describing the email to send. (required)
        :type public_single_send_request_egg: PublicSingleSendRequestEgg
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
        :rtype: EmailSendStatusView
        """
        kwargs["_return_http_data_only"] = True
        return self.send_email_with_http_info(public_single_send_request_egg, **kwargs)  # noqa: E501

    def send_email_with_http_info(self, public_single_send_request_egg, **kwargs):  # noqa: E501
        """Send a single transactional email asynchronously.  # noqa: E501

        Asynchronously send a transactional email. Returns the status of the email send with a statusId that can be used to continuously query for the status using the Email Send Status API.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_email_with_http_info(public_single_send_request_egg, async_req=True)
        >>> result = thread.get()

        :param public_single_send_request_egg: A request object describing the email to send. (required)
        :type public_single_send_request_egg: PublicSingleSendRequestEgg
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
        :rtype: tuple(EmailSendStatusView, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["public_single_send_request_egg"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method send_email" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'public_single_send_request_egg' is set
        if self.api_client.client_side_validation and local_var_params.get("public_single_send_request_egg") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `public_single_send_request_egg` when calling `send_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "public_single_send_request_egg" in local_var_params:
            body_params = local_var_params["public_single_send_request_egg"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "EmailSendStatusView",
        }

        return self.api_client.call_api(
            "/marketing/v3/transactional/single-email/send",
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
