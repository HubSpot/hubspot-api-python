# coding: utf-8

"""
    Forms

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

from hubspot.marketing.forms.configuration import Configuration


class LegalConsentOptionsLegitimateInterest(object):
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
    openapi_types = {"subscription_type_ids": "list[int]", "lawful_basis": "str", "type": "str", "privacy_text": "str"}

    attribute_map = {"subscription_type_ids": "subscriptionTypeIds", "lawful_basis": "lawfulBasis", "type": "type", "privacy_text": "privacyText"}

    def __init__(self, subscription_type_ids=None, lawful_basis=None, type="legitimate_interest", privacy_text=None, local_vars_configuration=None):  # noqa: E501
        """LegalConsentOptionsLegitimateInterest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._subscription_type_ids = None
        self._lawful_basis = None
        self._type = None
        self._privacy_text = None
        self.discriminator = None

        self.subscription_type_ids = subscription_type_ids
        self.lawful_basis = lawful_basis
        self.type = type
        self.privacy_text = privacy_text

    @property
    def subscription_type_ids(self):
        """Gets the subscription_type_ids of this LegalConsentOptionsLegitimateInterest.  # noqa: E501

          # noqa: E501

        :return: The subscription_type_ids of this LegalConsentOptionsLegitimateInterest.  # noqa: E501
        :rtype: list[int]
        """
        return self._subscription_type_ids

    @subscription_type_ids.setter
    def subscription_type_ids(self, subscription_type_ids):
        """Sets the subscription_type_ids of this LegalConsentOptionsLegitimateInterest.

          # noqa: E501

        :param subscription_type_ids: The subscription_type_ids of this LegalConsentOptionsLegitimateInterest.  # noqa: E501
        :type subscription_type_ids: list[int]
        """
        if self.local_vars_configuration.client_side_validation and subscription_type_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `subscription_type_ids`, must not be `None`")  # noqa: E501

        self._subscription_type_ids = subscription_type_ids

    @property
    def lawful_basis(self):
        """Gets the lawful_basis of this LegalConsentOptionsLegitimateInterest.  # noqa: E501

          # noqa: E501

        :return: The lawful_basis of this LegalConsentOptionsLegitimateInterest.  # noqa: E501
        :rtype: str
        """
        return self._lawful_basis

    @lawful_basis.setter
    def lawful_basis(self, lawful_basis):
        """Sets the lawful_basis of this LegalConsentOptionsLegitimateInterest.

          # noqa: E501

        :param lawful_basis: The lawful_basis of this LegalConsentOptionsLegitimateInterest.  # noqa: E501
        :type lawful_basis: str
        """
        if self.local_vars_configuration.client_side_validation and lawful_basis is None:  # noqa: E501
            raise ValueError("Invalid value for `lawful_basis`, must not be `None`")  # noqa: E501
        allowed_values = ["lead", "client", "other"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and lawful_basis not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `lawful_basis` ({0}), must be one of {1}".format(lawful_basis, allowed_values))  # noqa: E501

        self._lawful_basis = lawful_basis

    @property
    def type(self):
        """Gets the type of this LegalConsentOptionsLegitimateInterest.  # noqa: E501

          # noqa: E501

        :return: The type of this LegalConsentOptionsLegitimateInterest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LegalConsentOptionsLegitimateInterest.

          # noqa: E501

        :param type: The type of this LegalConsentOptionsLegitimateInterest.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["legitimate_interest"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `type` ({0}), must be one of {1}".format(type, allowed_values))  # noqa: E501

        self._type = type

    @property
    def privacy_text(self):
        """Gets the privacy_text of this LegalConsentOptionsLegitimateInterest.  # noqa: E501

          # noqa: E501

        :return: The privacy_text of this LegalConsentOptionsLegitimateInterest.  # noqa: E501
        :rtype: str
        """
        return self._privacy_text

    @privacy_text.setter
    def privacy_text(self, privacy_text):
        """Sets the privacy_text of this LegalConsentOptionsLegitimateInterest.

          # noqa: E501

        :param privacy_text: The privacy_text of this LegalConsentOptionsLegitimateInterest.  # noqa: E501
        :type privacy_text: str
        """
        if self.local_vars_configuration.client_side_validation and privacy_text is None:  # noqa: E501
            raise ValueError("Invalid value for `privacy_text`, must not be `None`")  # noqa: E501

        self._privacy_text = privacy_text

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
        if not isinstance(other, LegalConsentOptionsLegitimateInterest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LegalConsentOptionsLegitimateInterest):
            return True

        return self.to_dict() != other.to_dict()
