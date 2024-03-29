# coding: utf-8

"""
    CMS Url Redirects

    URL redirect operations  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.cms.url_redirects.configuration import Configuration


class UrlMappingCreateRequestBody(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "is_trailing_slash_optional": "bool",
        "is_match_query_string": "bool",
        "redirect_style": "int",
        "route_prefix": "str",
        "is_match_full_url": "bool",
        "is_protocol_agnostic": "bool",
        "destination": "str",
        "is_only_after_not_found": "bool",
        "is_pattern": "bool",
        "precedence": "int",
    }

    attribute_map = {
        "is_trailing_slash_optional": "isTrailingSlashOptional",
        "is_match_query_string": "isMatchQueryString",
        "redirect_style": "redirectStyle",
        "route_prefix": "routePrefix",
        "is_match_full_url": "isMatchFullUrl",
        "is_protocol_agnostic": "isProtocolAgnostic",
        "destination": "destination",
        "is_only_after_not_found": "isOnlyAfterNotFound",
        "is_pattern": "isPattern",
        "precedence": "precedence",
    }

    def __init__(
        self,
        is_trailing_slash_optional=None,
        is_match_query_string=None,
        redirect_style=None,
        route_prefix=None,
        is_match_full_url=None,
        is_protocol_agnostic=None,
        destination=None,
        is_only_after_not_found=None,
        is_pattern=None,
        precedence=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """UrlMappingCreateRequestBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._is_trailing_slash_optional = None
        self._is_match_query_string = None
        self._redirect_style = None
        self._route_prefix = None
        self._is_match_full_url = None
        self._is_protocol_agnostic = None
        self._destination = None
        self._is_only_after_not_found = None
        self._is_pattern = None
        self._precedence = None
        self.discriminator = None

        if is_trailing_slash_optional is not None:
            self.is_trailing_slash_optional = is_trailing_slash_optional
        if is_match_query_string is not None:
            self.is_match_query_string = is_match_query_string
        self.redirect_style = redirect_style
        self.route_prefix = route_prefix
        if is_match_full_url is not None:
            self.is_match_full_url = is_match_full_url
        if is_protocol_agnostic is not None:
            self.is_protocol_agnostic = is_protocol_agnostic
        self.destination = destination
        if is_only_after_not_found is not None:
            self.is_only_after_not_found = is_only_after_not_found
        if is_pattern is not None:
            self.is_pattern = is_pattern
        if precedence is not None:
            self.precedence = precedence

    @property
    def is_trailing_slash_optional(self):
        """Gets the is_trailing_slash_optional of this UrlMappingCreateRequestBody.  # noqa: E501


        :return: The is_trailing_slash_optional of this UrlMappingCreateRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_trailing_slash_optional

    @is_trailing_slash_optional.setter
    def is_trailing_slash_optional(self, is_trailing_slash_optional):
        """Sets the is_trailing_slash_optional of this UrlMappingCreateRequestBody.


        :param is_trailing_slash_optional: The is_trailing_slash_optional of this UrlMappingCreateRequestBody.  # noqa: E501
        :type is_trailing_slash_optional: bool
        """

        self._is_trailing_slash_optional = is_trailing_slash_optional

    @property
    def is_match_query_string(self):
        """Gets the is_match_query_string of this UrlMappingCreateRequestBody.  # noqa: E501


        :return: The is_match_query_string of this UrlMappingCreateRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_match_query_string

    @is_match_query_string.setter
    def is_match_query_string(self, is_match_query_string):
        """Sets the is_match_query_string of this UrlMappingCreateRequestBody.


        :param is_match_query_string: The is_match_query_string of this UrlMappingCreateRequestBody.  # noqa: E501
        :type is_match_query_string: bool
        """

        self._is_match_query_string = is_match_query_string

    @property
    def redirect_style(self):
        """Gets the redirect_style of this UrlMappingCreateRequestBody.  # noqa: E501


        :return: The redirect_style of this UrlMappingCreateRequestBody.  # noqa: E501
        :rtype: int
        """
        return self._redirect_style

    @redirect_style.setter
    def redirect_style(self, redirect_style):
        """Sets the redirect_style of this UrlMappingCreateRequestBody.


        :param redirect_style: The redirect_style of this UrlMappingCreateRequestBody.  # noqa: E501
        :type redirect_style: int
        """
        if self.local_vars_configuration.client_side_validation and redirect_style is None:  # noqa: E501
            raise ValueError("Invalid value for `redirect_style`, must not be `None`")  # noqa: E501

        self._redirect_style = redirect_style

    @property
    def route_prefix(self):
        """Gets the route_prefix of this UrlMappingCreateRequestBody.  # noqa: E501


        :return: The route_prefix of this UrlMappingCreateRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._route_prefix

    @route_prefix.setter
    def route_prefix(self, route_prefix):
        """Sets the route_prefix of this UrlMappingCreateRequestBody.


        :param route_prefix: The route_prefix of this UrlMappingCreateRequestBody.  # noqa: E501
        :type route_prefix: str
        """
        if self.local_vars_configuration.client_side_validation and route_prefix is None:  # noqa: E501
            raise ValueError("Invalid value for `route_prefix`, must not be `None`")  # noqa: E501

        self._route_prefix = route_prefix

    @property
    def is_match_full_url(self):
        """Gets the is_match_full_url of this UrlMappingCreateRequestBody.  # noqa: E501


        :return: The is_match_full_url of this UrlMappingCreateRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_match_full_url

    @is_match_full_url.setter
    def is_match_full_url(self, is_match_full_url):
        """Sets the is_match_full_url of this UrlMappingCreateRequestBody.


        :param is_match_full_url: The is_match_full_url of this UrlMappingCreateRequestBody.  # noqa: E501
        :type is_match_full_url: bool
        """

        self._is_match_full_url = is_match_full_url

    @property
    def is_protocol_agnostic(self):
        """Gets the is_protocol_agnostic of this UrlMappingCreateRequestBody.  # noqa: E501


        :return: The is_protocol_agnostic of this UrlMappingCreateRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_protocol_agnostic

    @is_protocol_agnostic.setter
    def is_protocol_agnostic(self, is_protocol_agnostic):
        """Sets the is_protocol_agnostic of this UrlMappingCreateRequestBody.


        :param is_protocol_agnostic: The is_protocol_agnostic of this UrlMappingCreateRequestBody.  # noqa: E501
        :type is_protocol_agnostic: bool
        """

        self._is_protocol_agnostic = is_protocol_agnostic

    @property
    def destination(self):
        """Gets the destination of this UrlMappingCreateRequestBody.  # noqa: E501


        :return: The destination of this UrlMappingCreateRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this UrlMappingCreateRequestBody.


        :param destination: The destination of this UrlMappingCreateRequestBody.  # noqa: E501
        :type destination: str
        """
        if self.local_vars_configuration.client_side_validation and destination is None:  # noqa: E501
            raise ValueError("Invalid value for `destination`, must not be `None`")  # noqa: E501

        self._destination = destination

    @property
    def is_only_after_not_found(self):
        """Gets the is_only_after_not_found of this UrlMappingCreateRequestBody.  # noqa: E501


        :return: The is_only_after_not_found of this UrlMappingCreateRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_only_after_not_found

    @is_only_after_not_found.setter
    def is_only_after_not_found(self, is_only_after_not_found):
        """Sets the is_only_after_not_found of this UrlMappingCreateRequestBody.


        :param is_only_after_not_found: The is_only_after_not_found of this UrlMappingCreateRequestBody.  # noqa: E501
        :type is_only_after_not_found: bool
        """

        self._is_only_after_not_found = is_only_after_not_found

    @property
    def is_pattern(self):
        """Gets the is_pattern of this UrlMappingCreateRequestBody.  # noqa: E501


        :return: The is_pattern of this UrlMappingCreateRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_pattern

    @is_pattern.setter
    def is_pattern(self, is_pattern):
        """Sets the is_pattern of this UrlMappingCreateRequestBody.


        :param is_pattern: The is_pattern of this UrlMappingCreateRequestBody.  # noqa: E501
        :type is_pattern: bool
        """

        self._is_pattern = is_pattern

    @property
    def precedence(self):
        """Gets the precedence of this UrlMappingCreateRequestBody.  # noqa: E501


        :return: The precedence of this UrlMappingCreateRequestBody.  # noqa: E501
        :rtype: int
        """
        return self._precedence

    @precedence.setter
    def precedence(self, precedence):
        """Sets the precedence of this UrlMappingCreateRequestBody.


        :param precedence: The precedence of this UrlMappingCreateRequestBody.  # noqa: E501
        :type precedence: int
        """

        self._precedence = precedence

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UrlMappingCreateRequestBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UrlMappingCreateRequestBody):
            return True

        return self.to_dict() != other.to_dict()
