# coding: utf-8

"""
    Lists

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

from hubspot.crm.lists.configuration import Configuration


class JoinTimeAndRecordId(object):
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
    openapi_types = {"record_id": "str", "membership_timestamp": "datetime"}

    attribute_map = {"record_id": "recordId", "membership_timestamp": "membershipTimestamp"}

    def __init__(self, record_id=None, membership_timestamp=None, local_vars_configuration=None):  # noqa: E501
        """JoinTimeAndRecordId - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._record_id = None
        self._membership_timestamp = None
        self.discriminator = None

        self.record_id = record_id
        self.membership_timestamp = membership_timestamp

    @property
    def record_id(self):
        """Gets the record_id of this JoinTimeAndRecordId.  # noqa: E501


        :return: The record_id of this JoinTimeAndRecordId.  # noqa: E501
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this JoinTimeAndRecordId.


        :param record_id: The record_id of this JoinTimeAndRecordId.  # noqa: E501
        :type record_id: str
        """
        if self.local_vars_configuration.client_side_validation and record_id is None:  # noqa: E501
            raise ValueError("Invalid value for `record_id`, must not be `None`")  # noqa: E501

        self._record_id = record_id

    @property
    def membership_timestamp(self):
        """Gets the membership_timestamp of this JoinTimeAndRecordId.  # noqa: E501


        :return: The membership_timestamp of this JoinTimeAndRecordId.  # noqa: E501
        :rtype: datetime
        """
        return self._membership_timestamp

    @membership_timestamp.setter
    def membership_timestamp(self, membership_timestamp):
        """Sets the membership_timestamp of this JoinTimeAndRecordId.


        :param membership_timestamp: The membership_timestamp of this JoinTimeAndRecordId.  # noqa: E501
        :type membership_timestamp: datetime
        """
        if self.local_vars_configuration.client_side_validation and membership_timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `membership_timestamp`, must not be `None`")  # noqa: E501

        self._membership_timestamp = membership_timestamp

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
        if not isinstance(other, JoinTimeAndRecordId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JoinTimeAndRecordId):
            return True

        return self.to_dict() != other.to_dict()
