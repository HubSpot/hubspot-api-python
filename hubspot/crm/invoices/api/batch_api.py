# coding: utf-8

"""
    Invoices

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool
from typing import Optional
from typing_extensions import Annotated
from hubspot.crm.invoices.models.batch_read_input_simple_public_object_id import BatchReadInputSimplePublicObjectId
from hubspot.crm.invoices.models.batch_response_simple_public_object import BatchResponseSimplePublicObject

from hubspot.crm.invoices.api_client import ApiClient, RequestSerialized
from hubspot.crm.invoices.api_response import ApiResponse
from hubspot.crm.invoices.rest import RESTResponseType


class BatchApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def post_crm_v3_objects_invoices_batch_read(
        self,
        batch_read_input_simple_public_object_id: BatchReadInputSimplePublicObjectId,
        archived: Annotated[Optional[StrictBool], Field(description="Whether to return only results that have been archived.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> BatchResponseSimplePublicObject:
        """Read a batch of invoices by internal ID, or unique property values


        :param batch_read_input_simple_public_object_id: (required)
        :type batch_read_input_simple_public_object_id: BatchReadInputSimplePublicObjectId
        :param archived: Whether to return only results that have been archived.
        :type archived: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_crm_v3_objects_invoices_batch_read_serialize(
            batch_read_input_simple_public_object_id=batch_read_input_simple_public_object_id,
            archived=archived,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BatchResponseSimplePublicObject",
            '207': "BatchResponseSimplePublicObjectWithErrors",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def post_crm_v3_objects_invoices_batch_read_with_http_info(
        self,
        batch_read_input_simple_public_object_id: BatchReadInputSimplePublicObjectId,
        archived: Annotated[Optional[StrictBool], Field(description="Whether to return only results that have been archived.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[BatchResponseSimplePublicObject]:
        """Read a batch of invoices by internal ID, or unique property values


        :param batch_read_input_simple_public_object_id: (required)
        :type batch_read_input_simple_public_object_id: BatchReadInputSimplePublicObjectId
        :param archived: Whether to return only results that have been archived.
        :type archived: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_crm_v3_objects_invoices_batch_read_serialize(
            batch_read_input_simple_public_object_id=batch_read_input_simple_public_object_id,
            archived=archived,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BatchResponseSimplePublicObject",
            '207': "BatchResponseSimplePublicObjectWithErrors",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def post_crm_v3_objects_invoices_batch_read_without_preload_content(
        self,
        batch_read_input_simple_public_object_id: BatchReadInputSimplePublicObjectId,
        archived: Annotated[Optional[StrictBool], Field(description="Whether to return only results that have been archived.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Read a batch of invoices by internal ID, or unique property values


        :param batch_read_input_simple_public_object_id: (required)
        :type batch_read_input_simple_public_object_id: BatchReadInputSimplePublicObjectId
        :param archived: Whether to return only results that have been archived.
        :type archived: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_crm_v3_objects_invoices_batch_read_serialize(
            batch_read_input_simple_public_object_id=batch_read_input_simple_public_object_id,
            archived=archived,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BatchResponseSimplePublicObject",
            '207': "BatchResponseSimplePublicObjectWithErrors",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _post_crm_v3_objects_invoices_batch_read_serialize(
        self,
        batch_read_input_simple_public_object_id,
        archived,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if archived is not None:
            
            _query_params.append(('archived', archived))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if batch_read_input_simple_public_object_id is not None:
            _body_params = batch_read_input_simple_public_object_id


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    '*/*'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'oauth2', 
            'private_apps'
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/crm/v3/objects/invoices/batch/read',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


