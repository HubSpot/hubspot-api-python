# coding: utf-8

"""
    Lists

    CRUD operations to manage lists and list memberships  # noqa: E501

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

from hubspot.crm.lists.configuration import Configuration


class PublicConstantFilter(object):
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
    openapi_types = {"filter_type": "str", "should_accept": "bool", "source": "str"}

    attribute_map = {"filter_type": "filterType", "should_accept": "shouldAccept", "source": "source"}

    def __init__(self, filter_type="CONSTANT", should_accept=None, source=None, local_vars_configuration=None):  # noqa: E501
        """PublicConstantFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._filter_type = None
        self._should_accept = None
        self._source = None
        self.discriminator = None

        self.filter_type = filter_type
        self.should_accept = should_accept
        if source is not None:
            self.source = source

    @property
    def filter_type(self):
        """Gets the filter_type of this PublicConstantFilter.  # noqa: E501


        :return: The filter_type of this PublicConstantFilter.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this PublicConstantFilter.


        :param filter_type: The filter_type of this PublicConstantFilter.  # noqa: E501
        :type filter_type: str
        """
        if self.local_vars_configuration.client_side_validation and filter_type is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_type`, must not be `None`")  # noqa: E501
        allowed_values = ["CONSTANT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and filter_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `filter_type` ({0}), must be one of {1}".format(filter_type, allowed_values))  # noqa: E501

        self._filter_type = filter_type

    @property
    def should_accept(self):
        """Gets the should_accept of this PublicConstantFilter.  # noqa: E501


        :return: The should_accept of this PublicConstantFilter.  # noqa: E501
        :rtype: bool
        """
        return self._should_accept

    @should_accept.setter
    def should_accept(self, should_accept):
        """Sets the should_accept of this PublicConstantFilter.


        :param should_accept: The should_accept of this PublicConstantFilter.  # noqa: E501
        :type should_accept: bool
        """
        if self.local_vars_configuration.client_side_validation and should_accept is None:  # noqa: E501
            raise ValueError("Invalid value for `should_accept`, must not be `None`")  # noqa: E501

        self._should_accept = should_accept

    @property
    def source(self):
        """Gets the source of this PublicConstantFilter.  # noqa: E501


        :return: The source of this PublicConstantFilter.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PublicConstantFilter.


        :param source: The source of this PublicConstantFilter.  # noqa: E501
        :type source: str
        """

        self._source = source

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
        if not isinstance(other, PublicConstantFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicConstantFilter):
            return True

        return self.to_dict() != other.to_dict()