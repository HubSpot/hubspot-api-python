# coding: utf-8

"""
    Hubdb

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

from hubspot.cms.hubdb.configuration import Configuration


class RandomAccessCollectionResponseWithTotalHubDbTableRowV3(object):
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
    openapi_types = {"total": "int", "paging": "BoundedPaging", "type": "str", "results": "list[HubDbTableRowV3]"}

    attribute_map = {"total": "total", "paging": "paging", "type": "type", "results": "results"}

    def __init__(self, total=None, paging=None, type="RANDOM_ACCESS", results=None, local_vars_configuration=None):  # noqa: E501
        """RandomAccessCollectionResponseWithTotalHubDbTableRowV3 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._paging = None
        self._type = None
        self._results = None
        self.discriminator = None

        self.total = total
        if paging is not None:
            self.paging = paging
        self.type = type
        self.results = results

    @property
    def total(self):
        """Gets the total of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.  # noqa: E501


        :return: The total of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.


        :param total: The total of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.  # noqa: E501
        :type total: int
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def paging(self):
        """Gets the paging of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.  # noqa: E501


        :return: The paging of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.  # noqa: E501
        :rtype: BoundedPaging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.


        :param paging: The paging of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.  # noqa: E501
        :type paging: BoundedPaging
        """

        self._paging = paging

    @property
    def type(self):
        """Gets the type of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.  # noqa: E501


        :return: The type of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.


        :param type: The type of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["RANDOM_ACCESS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `type` ({0}), must be one of {1}".format(type, allowed_values))  # noqa: E501

        self._type = type

    @property
    def results(self):
        """Gets the results of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.  # noqa: E501


        :return: The results of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.  # noqa: E501
        :rtype: list[HubDbTableRowV3]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.


        :param results: The results of this RandomAccessCollectionResponseWithTotalHubDbTableRowV3.  # noqa: E501
        :type results: list[HubDbTableRowV3]
        """
        if self.local_vars_configuration.client_side_validation and results is None:  # noqa: E501
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

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
        if not isinstance(other, RandomAccessCollectionResponseWithTotalHubDbTableRowV3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RandomAccessCollectionResponseWithTotalHubDbTableRowV3):
            return True

        return self.to_dict() != other.to_dict()
