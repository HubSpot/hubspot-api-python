"""
    CRM cards

    Allows an app to extend the CRM UI by surfacing custom cards in the sidebar of record pages. These cards are defined up-front as part of app configuration, then populated by external data fetch requests when the record page is accessed by a user.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.cards.configuration import Configuration


class DisplayOption:
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
    openapi_types = {"name": "str", "label": "str", "type": "str"}

    attribute_map = {"name": "name", "label": "label", "type": "type"}

    def __init__(
        self, name=None, label=None, type=None, local_vars_configuration=None
    ):  # noqa: E501
        """DisplayOption - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._label = None
        self._type = None
        self.discriminator = None

        self.name = name
        self.label = label
        self.type = type

    @property
    def name(self):
        """Gets the name of this DisplayOption.  # noqa: E501

        JSON-friendly unique name for option.  # noqa: E501

        :return: The name of this DisplayOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DisplayOption.

        JSON-friendly unique name for option.  # noqa: E501

        :param name: The name of this DisplayOption.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def label(self):
        """Gets the label of this DisplayOption.  # noqa: E501

        The text that will be displayed to users for this option.  # noqa: E501

        :return: The label of this DisplayOption.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DisplayOption.

        The text that will be displayed to users for this option.  # noqa: E501

        :param label: The label of this DisplayOption.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and label is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `label`, must not be `None`"
            )  # noqa: E501

        self._label = label

    @property
    def type(self):
        """Gets the type of this DisplayOption.  # noqa: E501

        The type of status.  # noqa: E501

        :return: The type of this DisplayOption.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DisplayOption.

        The type of status.  # noqa: E501

        :param type: The type of this DisplayOption.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "DEFAULT",
            "SUCCESS",
            "WARNING",
            "DANGER",
            "INFO",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({}), must be one of {}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DisplayOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DisplayOption):
            return True

        return self.to_dict() != other.to_dict()
