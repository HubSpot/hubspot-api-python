"""
    Timeline events

    This feature allows an app to create and configure custom events that can show up in the timelines of certain CRM objects like contacts, companies, tickets, or deals. You'll find multiple use cases for this API in the sections below.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""



import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.timeline.api_client import ApiClient
from hubspot.crm.timeline.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class TokensApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, event_template_id, token_name, app_id, **kwargs):  # noqa: E501
        """Removes a token from the event template  # noqa: E501

        This will remove the token from an existing template. Existing events and CRM objects will still retain the token and its mapped object properties, but new ones will not.  The timeline will still display this property for older CRM objects if it's still referenced in the template `Markdown`. New events will not.  Any lists or reports referencing deleted tokens will no longer return new contacts, but old ones will still exist in the lists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive(event_template_id, token_name, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param str token_name: The token name. (required)
        :param int app_id: The ID of the target app. (required)
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
        return self.archive_with_http_info(
            event_template_id, token_name, app_id, **kwargs
        )  # noqa: E501

    def archive_with_http_info(
        self, event_template_id, token_name, app_id, **kwargs
    ):  # noqa: E501
        """Removes a token from the event template  # noqa: E501

        This will remove the token from an existing template. Existing events and CRM objects will still retain the token and its mapped object properties, but new ones will not.  The timeline will still display this property for older CRM objects if it's still referenced in the template `Markdown`. New events will not.  Any lists or reports referencing deleted tokens will no longer return new contacts, but old ones will still exist in the lists.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_with_http_info(event_template_id, token_name, app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param str token_name: The token name. (required)
        :param int app_id: The ID of the target app. (required)
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

        all_params = ["event_template_id", "token_name", "app_id"]
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
        # verify the required parameter 'event_template_id' is set
        if self.api_client.client_side_validation and (
            "event_template_id" not in local_var_params
            or local_var_params["event_template_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `event_template_id` when calling `archive`"
            )  # noqa: E501
        # verify the required parameter 'token_name' is set
        if self.api_client.client_side_validation and (
            "token_name" not in local_var_params
            or local_var_params["token_name"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `token_name` when calling `archive`"
            )  # noqa: E501
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `archive`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "event_template_id" in local_var_params:
            path_params["eventTemplateId"] = local_var_params[
                "event_template_id"
            ]  # noqa: E501
        if "token_name" in local_var_params:
            path_params["tokenName"] = local_var_params["token_name"]  # noqa: E501
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

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
        auth_settings = ["developer_hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}/tokens/{tokenName}",
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

    def create(
        self, event_template_id, app_id, timeline_event_template_token, **kwargs
    ):  # noqa: E501
        """Adds a token to an existing event template  # noqa: E501

        Once you've defined an event template, it's likely that you'll want to define tokens for it as well. You can do this on the event template itself or update individual tokens here.  Event type tokens allow you to attach custom data to events displayed in a timeline or used for list segmentation.  You can also use `objectPropertyName` to associate any CRM object properties. This will allow you to fully build out CRM objects.  Token names should be unique across the template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(event_template_id, app_id, timeline_event_template_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param int app_id: The ID of the target app. (required)
        :param TimelineEventTemplateToken timeline_event_template_token: The new token definition. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TimelineEventTemplateToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.create_with_http_info(
            event_template_id, app_id, timeline_event_template_token, **kwargs
        )  # noqa: E501

    def create_with_http_info(
        self, event_template_id, app_id, timeline_event_template_token, **kwargs
    ):  # noqa: E501
        """Adds a token to an existing event template  # noqa: E501

        Once you've defined an event template, it's likely that you'll want to define tokens for it as well. You can do this on the event template itself or update individual tokens here.  Event type tokens allow you to attach custom data to events displayed in a timeline or used for list segmentation.  You can also use `objectPropertyName` to associate any CRM object properties. This will allow you to fully build out CRM objects.  Token names should be unique across the template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(event_template_id, app_id, timeline_event_template_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param int app_id: The ID of the target app. (required)
        :param TimelineEventTemplateToken timeline_event_template_token: The new token definition. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TimelineEventTemplateToken, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ["event_template_id", "app_id", "timeline_event_template_token"]
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
        # verify the required parameter 'event_template_id' is set
        if self.api_client.client_side_validation and (
            "event_template_id" not in local_var_params
            or local_var_params["event_template_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `event_template_id` when calling `create`"
            )  # noqa: E501
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `create`"
            )  # noqa: E501
        # verify the required parameter 'timeline_event_template_token' is set
        if self.api_client.client_side_validation and (
            "timeline_event_template_token" not in local_var_params
            or local_var_params["timeline_event_template_token"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `timeline_event_template_token` when calling `create`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "event_template_id" in local_var_params:
            path_params["eventTemplateId"] = local_var_params[
                "event_template_id"
            ]  # noqa: E501
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "timeline_event_template_token" in local_var_params:
            body_params = local_var_params["timeline_event_template_token"]
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
        auth_settings = ["developer_hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}/tokens",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="TimelineEventTemplateToken",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update(
        self,
        event_template_id,
        token_name,
        app_id,
        timeline_event_template_token_update_request,
        **kwargs
    ):  # noqa: E501
        """Updates an existing token on an event template  # noqa: E501

        This will update the existing token on an event template. Name and type can't be changed on existing tokens.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(event_template_id, token_name, app_id, timeline_event_template_token_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param str token_name: The token name. (required)
        :param int app_id: The ID of the target app. (required)
        :param TimelineEventTemplateTokenUpdateRequest timeline_event_template_token_update_request: The updated token definition. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TimelineEventTemplateToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        return self.update_with_http_info(
            event_template_id,
            token_name,
            app_id,
            timeline_event_template_token_update_request,
            **kwargs
        )  # noqa: E501

    def update_with_http_info(
        self,
        event_template_id,
        token_name,
        app_id,
        timeline_event_template_token_update_request,
        **kwargs
    ):  # noqa: E501
        """Updates an existing token on an event template  # noqa: E501

        This will update the existing token on an event template. Name and type can't be changed on existing tokens.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(event_template_id, token_name, app_id, timeline_event_template_token_update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str event_template_id: The event template ID. (required)
        :param str token_name: The token name. (required)
        :param int app_id: The ID of the target app. (required)
        :param TimelineEventTemplateTokenUpdateRequest timeline_event_template_token_update_request: The updated token definition. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TimelineEventTemplateToken, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            "event_template_id",
            "token_name",
            "app_id",
            "timeline_event_template_token_update_request",
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
                    "Got an unexpected keyword argument '%s'" " to method update" % key
                )
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'event_template_id' is set
        if self.api_client.client_side_validation and (
            "event_template_id" not in local_var_params
            or local_var_params["event_template_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `event_template_id` when calling `update`"
            )  # noqa: E501
        # verify the required parameter 'token_name' is set
        if self.api_client.client_side_validation and (
            "token_name" not in local_var_params
            or local_var_params["token_name"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `token_name` when calling `update`"
            )  # noqa: E501
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and (
            "app_id" not in local_var_params
            or local_var_params["app_id"] is None  # noqa: E501
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `app_id` when calling `update`"
            )  # noqa: E501
        # verify the required parameter 'timeline_event_template_token_update_request' is set
        if self.api_client.client_side_validation and (
            "timeline_event_template_token_update_request" not in local_var_params
            or local_var_params[  # noqa: E501
                "timeline_event_template_token_update_request"
            ]
            is None
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `timeline_event_template_token_update_request` when calling `update`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "event_template_id" in local_var_params:
            path_params["eventTemplateId"] = local_var_params[
                "event_template_id"
            ]  # noqa: E501
        if "token_name" in local_var_params:
            path_params["tokenName"] = local_var_params["token_name"]  # noqa: E501
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "timeline_event_template_token_update_request" in local_var_params:
            body_params = local_var_params[
                "timeline_event_template_token_update_request"
            ]
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
        auth_settings = ["developer_hapikey"]  # noqa: E501

        return self.api_client.call_api(
            "/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}/tokens/{tokenName}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="TimelineEventTemplateToken",  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get(
                "_return_http_data_only"
            ),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
