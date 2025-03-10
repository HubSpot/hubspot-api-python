# coding: utf-8

"""
    Marketing Events

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

from hubspot.marketing.events.configuration import Configuration


class MarketingEventSubscriber(object):
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
    openapi_types = {"vid": "int", "properties": "dict[str, str]", "interaction_date_time": "int"}

    attribute_map = {"vid": "vid", "properties": "properties", "interaction_date_time": "interactionDateTime"}

    def __init__(self, vid=None, properties=None, interaction_date_time=None, local_vars_configuration=None):  # noqa: E501
        """MarketingEventSubscriber - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._vid = None
        self._properties = None
        self._interaction_date_time = None
        self.discriminator = None

        if vid is not None:
            self.vid = vid
        if properties is not None:
            self.properties = properties
        self.interaction_date_time = interaction_date_time

    @property
    def vid(self):
        """Gets the vid of this MarketingEventSubscriber.  # noqa: E501


        :return: The vid of this MarketingEventSubscriber.  # noqa: E501
        :rtype: int
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """Sets the vid of this MarketingEventSubscriber.


        :param vid: The vid of this MarketingEventSubscriber.  # noqa: E501
        :type vid: int
        """

        self._vid = vid

    @property
    def properties(self):
        """Gets the properties of this MarketingEventSubscriber.  # noqa: E501


        :return: The properties of this MarketingEventSubscriber.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this MarketingEventSubscriber.


        :param properties: The properties of this MarketingEventSubscriber.  # noqa: E501
        :type properties: dict[str, str]
        """

        self._properties = properties

    @property
    def interaction_date_time(self):
        """Gets the interaction_date_time of this MarketingEventSubscriber.  # noqa: E501

        The date and time at which the contact subscribed to the event.  # noqa: E501

        :return: The interaction_date_time of this MarketingEventSubscriber.  # noqa: E501
        :rtype: int
        """
        return self._interaction_date_time

    @interaction_date_time.setter
    def interaction_date_time(self, interaction_date_time):
        """Sets the interaction_date_time of this MarketingEventSubscriber.

        The date and time at which the contact subscribed to the event.  # noqa: E501

        :param interaction_date_time: The interaction_date_time of this MarketingEventSubscriber.  # noqa: E501
        :type interaction_date_time: int
        """
        if self.local_vars_configuration.client_side_validation and interaction_date_time is None:  # noqa: E501
            raise ValueError("Invalid value for `interaction_date_time`, must not be `None`")  # noqa: E501

        self._interaction_date_time = interaction_date_time

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
        if not isinstance(other, MarketingEventSubscriber):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarketingEventSubscriber):
            return True

        return self.to_dict() != other.to_dict()
