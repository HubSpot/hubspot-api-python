"""
    CMS Performance API

    Use these endpoints to get a time series view of your website's performance.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.performance.configuration import Configuration


class PublicPerformanceResponse:
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
        "data": "list[PerformanceView]",
        "domain": "str",
        "path": "str",
        "start_interval": "int",
        "end_interval": "int",
        "interval": "str",
        "period": "str",
    }

    attribute_map = {
        "data": "data",
        "domain": "domain",
        "path": "path",
        "start_interval": "startInterval",
        "end_interval": "endInterval",
        "interval": "interval",
        "period": "period",
    }

    def __init__(
        self,
        data=None,
        domain=None,
        path=None,
        start_interval=None,
        end_interval=None,
        interval=None,
        period=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """PublicPerformanceResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._data = None
        self._domain = None
        self._path = None
        self._start_interval = None
        self._end_interval = None
        self._interval = None
        self._period = None
        self.discriminator = None

        self.data = data
        if domain is not None:
            self.domain = domain
        if path is not None:
            self.path = path
        self.start_interval = start_interval
        self.end_interval = end_interval
        self.interval = interval
        if period is not None:
            self.period = period

    @property
    def data(self):
        """Gets the data of this PublicPerformanceResponse.  # noqa: E501


        :return: The data of this PublicPerformanceResponse.  # noqa: E501
        :rtype: list[PerformanceView]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PublicPerformanceResponse.


        :param data: The data of this PublicPerformanceResponse.  # noqa: E501
        :type: list[PerformanceView]
        """
        if (
            self.local_vars_configuration.client_side_validation and data is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `data`, must not be `None`"
            )  # noqa: E501

        self._data = data

    @property
    def domain(self):
        """Gets the domain of this PublicPerformanceResponse.  # noqa: E501


        :return: The domain of this PublicPerformanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this PublicPerformanceResponse.


        :param domain: The domain of this PublicPerformanceResponse.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def path(self):
        """Gets the path of this PublicPerformanceResponse.  # noqa: E501


        :return: The path of this PublicPerformanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PublicPerformanceResponse.


        :param path: The path of this PublicPerformanceResponse.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def start_interval(self):
        """Gets the start_interval of this PublicPerformanceResponse.  # noqa: E501


        :return: The start_interval of this PublicPerformanceResponse.  # noqa: E501
        :rtype: int
        """
        return self._start_interval

    @start_interval.setter
    def start_interval(self, start_interval):
        """Sets the start_interval of this PublicPerformanceResponse.


        :param start_interval: The start_interval of this PublicPerformanceResponse.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and start_interval is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `start_interval`, must not be `None`"
            )  # noqa: E501

        self._start_interval = start_interval

    @property
    def end_interval(self):
        """Gets the end_interval of this PublicPerformanceResponse.  # noqa: E501


        :return: The end_interval of this PublicPerformanceResponse.  # noqa: E501
        :rtype: int
        """
        return self._end_interval

    @end_interval.setter
    def end_interval(self, end_interval):
        """Sets the end_interval of this PublicPerformanceResponse.


        :param end_interval: The end_interval of this PublicPerformanceResponse.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation
            and end_interval is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `end_interval`, must not be `None`"
            )  # noqa: E501

        self._end_interval = end_interval

    @property
    def interval(self):
        """Gets the interval of this PublicPerformanceResponse.  # noqa: E501


        :return: The interval of this PublicPerformanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this PublicPerformanceResponse.


        :param interval: The interval of this PublicPerformanceResponse.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and interval is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `interval`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "ONE_MINUTE",
            "FIVE_MINUTES",
            "TEN_MINUTES",
            "FIFTEEN_MINUTES",
            "THIRTY_MINUTES",
            "ONE_HOUR",
            "FOUR_HOURS",
            "TWELVE_HOURS",
            "ONE_DAY",
            "ONE_WEEK",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and interval not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `interval` ({}), must be one of {}".format(  # noqa: E501
                    interval, allowed_values
                )
            )

        self._interval = interval

    @property
    def period(self):
        """Gets the period of this PublicPerformanceResponse.  # noqa: E501


        :return: The period of this PublicPerformanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this PublicPerformanceResponse.


        :param period: The period of this PublicPerformanceResponse.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "ONE_MINUTE",
            "FIVE_MINUTES",
            "TEN_MINUTES",
            "FIFTEEN_MINUTES",
            "THIRTY_MINUTES",
            "ONE_HOUR",
            "FOUR_HOURS",
            "TWELVE_HOURS",
            "ONE_DAY",
            "ONE_WEEK",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and period not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `period` ({}), must be one of {}".format(  # noqa: E501
                    period, allowed_values
                )
            )

        self._period = period

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
        if not isinstance(other, PublicPerformanceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicPerformanceResponse):
            return True

        return self.to_dict() != other.to_dict()
