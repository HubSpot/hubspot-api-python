# coding: utf-8

"""
    Public App Crm Cards

    Allows an app to extend the CRM UI by surfacing custom cards in the sidebar of record pages. These cards are defined up-front as part of app configuration, then populated by external data fetch requests when the record page is accessed by a user.  # noqa: E501

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

from hubspot.crm.extensions.cards.configuration import Configuration


class CardObjectTypeBody(object):
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
    openapi_types = {"name": "str", "properties_to_send": "list[str]"}

    attribute_map = {"name": "name", "properties_to_send": "propertiesToSend"}

    def __init__(self, name=None, properties_to_send=None, local_vars_configuration=None):  # noqa: E501
        """CardObjectTypeBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._properties_to_send = None
        self.discriminator = None

        self.name = name
        self.properties_to_send = properties_to_send

    @property
    def name(self):
        """Gets the name of this CardObjectTypeBody.  # noqa: E501

        A CRM object type where this card should be displayed.  # noqa: E501

        :return: The name of this CardObjectTypeBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CardObjectTypeBody.

        A CRM object type where this card should be displayed.  # noqa: E501

        :param name: The name of this CardObjectTypeBody.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        allowed_values = ["contacts", "deals", "companies", "tickets", "marketing_events"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and name not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `name` ({0}), must be one of {1}".format(name, allowed_values))  # noqa: E501

        self._name = name

    @property
    def properties_to_send(self):
        """Gets the properties_to_send of this CardObjectTypeBody.  # noqa: E501

        An array of properties that should be sent to this card's target URL when the data fetch request is made. Must be valid properties for the corresponding CRM object type.  # noqa: E501

        :return: The properties_to_send of this CardObjectTypeBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._properties_to_send

    @properties_to_send.setter
    def properties_to_send(self, properties_to_send):
        """Sets the properties_to_send of this CardObjectTypeBody.

        An array of properties that should be sent to this card's target URL when the data fetch request is made. Must be valid properties for the corresponding CRM object type.  # noqa: E501

        :param properties_to_send: The properties_to_send of this CardObjectTypeBody.  # noqa: E501
        :type properties_to_send: list[str]
        """
        if self.local_vars_configuration.client_side_validation and properties_to_send is None:  # noqa: E501
            raise ValueError("Invalid value for `properties_to_send`, must not be `None`")  # noqa: E501

        self._properties_to_send = properties_to_send

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
        if not isinstance(other, CardObjectTypeBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CardObjectTypeBody):
            return True

        return self.to_dict() != other.to_dict()
