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


class MarketingEventCompleteRequestParams(object):
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
    openapi_types = {"start_date_time": "datetime", "end_date_time": "datetime"}

    attribute_map = {"start_date_time": "startDateTime", "end_date_time": "endDateTime"}

    def __init__(self, start_date_time=None, end_date_time=None, local_vars_configuration=None):  # noqa: E501
        """MarketingEventCompleteRequestParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date_time = None
        self._end_date_time = None
        self.discriminator = None

        self.start_date_time = start_date_time
        self.end_date_time = end_date_time

    @property
    def start_date_time(self):
        """Gets the start_date_time of this MarketingEventCompleteRequestParams.  # noqa: E501


        :return: The start_date_time of this MarketingEventCompleteRequestParams.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this MarketingEventCompleteRequestParams.


        :param start_date_time: The start_date_time of this MarketingEventCompleteRequestParams.  # noqa: E501
        :type start_date_time: datetime
        """
        if self.local_vars_configuration.client_side_validation and start_date_time is None:  # noqa: E501
            raise ValueError("Invalid value for `start_date_time`, must not be `None`")  # noqa: E501

        self._start_date_time = start_date_time

    @property
    def end_date_time(self):
        """Gets the end_date_time of this MarketingEventCompleteRequestParams.  # noqa: E501


        :return: The end_date_time of this MarketingEventCompleteRequestParams.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this MarketingEventCompleteRequestParams.


        :param end_date_time: The end_date_time of this MarketingEventCompleteRequestParams.  # noqa: E501
        :type end_date_time: datetime
        """
        if self.local_vars_configuration.client_side_validation and end_date_time is None:  # noqa: E501
            raise ValueError("Invalid value for `end_date_time`, must not be `None`")  # noqa: E501

        self._end_date_time = end_date_time

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
        if not isinstance(other, MarketingEventCompleteRequestParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarketingEventCompleteRequestParams):
            return True

        return self.to_dict() != other.to_dict()
