# coding: utf-8

"""
    Automation Actions V4

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.automation.actions.configuration import Configuration


class Option(object):
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
    openapi_types = {"hidden": "bool", "display_order": "int", "double_data": "float", "description": "str", "read_only": "bool", "label": "str", "value": "str"}

    attribute_map = {"hidden": "hidden", "display_order": "displayOrder", "double_data": "doubleData", "description": "description", "read_only": "readOnly", "label": "label", "value": "value"}

    def __init__(self, hidden=None, display_order=None, double_data=None, description=None, read_only=None, label=None, value=None, local_vars_configuration=None):  # noqa: E501
        """Option - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._hidden = None
        self._display_order = None
        self._double_data = None
        self._description = None
        self._read_only = None
        self._label = None
        self._value = None
        self.discriminator = None

        self.hidden = hidden
        self.display_order = display_order
        self.double_data = double_data
        self.description = description
        self.read_only = read_only
        self.label = label
        self.value = value

    @property
    def hidden(self):
        """Gets the hidden of this Option.  # noqa: E501


        :return: The hidden of this Option.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Option.


        :param hidden: The hidden of this Option.  # noqa: E501
        :type hidden: bool
        """
        if self.local_vars_configuration.client_side_validation and hidden is None:  # noqa: E501
            raise ValueError("Invalid value for `hidden`, must not be `None`")  # noqa: E501

        self._hidden = hidden

    @property
    def display_order(self):
        """Gets the display_order of this Option.  # noqa: E501


        :return: The display_order of this Option.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this Option.


        :param display_order: The display_order of this Option.  # noqa: E501
        :type display_order: int
        """
        if self.local_vars_configuration.client_side_validation and display_order is None:  # noqa: E501
            raise ValueError("Invalid value for `display_order`, must not be `None`")  # noqa: E501

        self._display_order = display_order

    @property
    def double_data(self):
        """Gets the double_data of this Option.  # noqa: E501


        :return: The double_data of this Option.  # noqa: E501
        :rtype: float
        """
        return self._double_data

    @double_data.setter
    def double_data(self, double_data):
        """Sets the double_data of this Option.


        :param double_data: The double_data of this Option.  # noqa: E501
        :type double_data: float
        """
        if self.local_vars_configuration.client_side_validation and double_data is None:  # noqa: E501
            raise ValueError("Invalid value for `double_data`, must not be `None`")  # noqa: E501

        self._double_data = double_data

    @property
    def description(self):
        """Gets the description of this Option.  # noqa: E501


        :return: The description of this Option.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Option.


        :param description: The description of this Option.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def read_only(self):
        """Gets the read_only of this Option.  # noqa: E501


        :return: The read_only of this Option.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this Option.


        :param read_only: The read_only of this Option.  # noqa: E501
        :type read_only: bool
        """
        if self.local_vars_configuration.client_side_validation and read_only is None:  # noqa: E501
            raise ValueError("Invalid value for `read_only`, must not be `None`")  # noqa: E501

        self._read_only = read_only

    @property
    def label(self):
        """Gets the label of this Option.  # noqa: E501


        :return: The label of this Option.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Option.


        :param label: The label of this Option.  # noqa: E501
        :type label: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def value(self):
        """Gets the value of this Option.  # noqa: E501


        :return: The value of this Option.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Option.


        :param value: The value of this Option.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, Option):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Option):
            return True

        return self.to_dict() != other.to_dict()
