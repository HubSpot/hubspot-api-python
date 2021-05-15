"""
    Blog Post endpoints

    \"Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags\"  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.blogs.tags.configuration import Configuration


class BatchInputString:
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
    openapi_types = {"inputs": "list[str]"}

    attribute_map = {"inputs": "inputs"}

    def __init__(self, inputs=None, local_vars_configuration=None):  # noqa: E501
        """BatchInputString - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._inputs = None
        self.discriminator = None

        self.inputs = inputs

    @property
    def inputs(self):
        """Gets the inputs of this BatchInputString.  # noqa: E501


        :return: The inputs of this BatchInputString.  # noqa: E501
        :rtype: list[str]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this BatchInputString.


        :param inputs: The inputs of this BatchInputString.  # noqa: E501
        :type: list[str]
        """
        if (
            self.local_vars_configuration.client_side_validation and inputs is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `inputs`, must not be `None`"
            )  # noqa: E501

        self._inputs = inputs

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
        if not isinstance(other, BatchInputString):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchInputString):
            return True

        return self.to_dict() != other.to_dict()
