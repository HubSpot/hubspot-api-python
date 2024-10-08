# coding: utf-8

"""
    Communication Preferences Subscriptions

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

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

from hubspot.communication_preferences.configuration import Configuration


class SubscriptionDefinitionsResponse(object):
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
    openapi_types = {"subscription_definitions": "list[SubscriptionDefinition]"}

    attribute_map = {"subscription_definitions": "subscriptionDefinitions"}

    def __init__(self, subscription_definitions=None, local_vars_configuration=None):  # noqa: E501
        """SubscriptionDefinitionsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._subscription_definitions = None
        self.discriminator = None

        self.subscription_definitions = subscription_definitions

    @property
    def subscription_definitions(self):
        """Gets the subscription_definitions of this SubscriptionDefinitionsResponse.  # noqa: E501

        A list of all subscription definitions.  # noqa: E501

        :return: The subscription_definitions of this SubscriptionDefinitionsResponse.  # noqa: E501
        :rtype: list[SubscriptionDefinition]
        """
        return self._subscription_definitions

    @subscription_definitions.setter
    def subscription_definitions(self, subscription_definitions):
        """Sets the subscription_definitions of this SubscriptionDefinitionsResponse.

        A list of all subscription definitions.  # noqa: E501

        :param subscription_definitions: The subscription_definitions of this SubscriptionDefinitionsResponse.  # noqa: E501
        :type subscription_definitions: list[SubscriptionDefinition]
        """
        if self.local_vars_configuration.client_side_validation and subscription_definitions is None:  # noqa: E501
            raise ValueError("Invalid value for `subscription_definitions`, must not be `None`")  # noqa: E501

        self._subscription_definitions = subscription_definitions

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
        if not isinstance(other, SubscriptionDefinitionsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionDefinitionsResponse):
            return True

        return self.to_dict() != other.to_dict()
