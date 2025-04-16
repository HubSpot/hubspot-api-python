# coding: utf-8

"""
    Marketing Emails

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

from hubspot.marketing.emails.configuration import Configuration


class PublicEmailSubscriptionDetails(object):
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
    openapi_types = {"office_location_id": "str", "preferences_group_id": "str", "subscription_id": "str"}

    attribute_map = {"office_location_id": "officeLocationId", "preferences_group_id": "preferencesGroupId", "subscription_id": "subscriptionId"}

    def __init__(self, office_location_id=None, preferences_group_id=None, subscription_id=None, local_vars_configuration=None):  # noqa: E501
        """PublicEmailSubscriptionDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._office_location_id = None
        self._preferences_group_id = None
        self._subscription_id = None
        self.discriminator = None

        if office_location_id is not None:
            self.office_location_id = office_location_id
        if preferences_group_id is not None:
            self.preferences_group_id = preferences_group_id
        if subscription_id is not None:
            self.subscription_id = subscription_id

    @property
    def office_location_id(self):
        """Gets the office_location_id of this PublicEmailSubscriptionDetails.  # noqa: E501

        ID of the selected office location.  # noqa: E501

        :return: The office_location_id of this PublicEmailSubscriptionDetails.  # noqa: E501
        :rtype: str
        """
        return self._office_location_id

    @office_location_id.setter
    def office_location_id(self, office_location_id):
        """Sets the office_location_id of this PublicEmailSubscriptionDetails.

        ID of the selected office location.  # noqa: E501

        :param office_location_id: The office_location_id of this PublicEmailSubscriptionDetails.  # noqa: E501
        :type office_location_id: str
        """

        self._office_location_id = office_location_id

    @property
    def preferences_group_id(self):
        """Gets the preferences_group_id of this PublicEmailSubscriptionDetails.  # noqa: E501

          # noqa: E501

        :return: The preferences_group_id of this PublicEmailSubscriptionDetails.  # noqa: E501
        :rtype: str
        """
        return self._preferences_group_id

    @preferences_group_id.setter
    def preferences_group_id(self, preferences_group_id):
        """Sets the preferences_group_id of this PublicEmailSubscriptionDetails.

          # noqa: E501

        :param preferences_group_id: The preferences_group_id of this PublicEmailSubscriptionDetails.  # noqa: E501
        :type preferences_group_id: str
        """

        self._preferences_group_id = preferences_group_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this PublicEmailSubscriptionDetails.  # noqa: E501

        ID of the subscription.  # noqa: E501

        :return: The subscription_id of this PublicEmailSubscriptionDetails.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this PublicEmailSubscriptionDetails.

        ID of the subscription.  # noqa: E501

        :param subscription_id: The subscription_id of this PublicEmailSubscriptionDetails.  # noqa: E501
        :type subscription_id: str
        """

        self._subscription_id = subscription_id

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
        if not isinstance(other, PublicEmailSubscriptionDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicEmailSubscriptionDetails):
            return True

        return self.to_dict() != other.to_dict()
