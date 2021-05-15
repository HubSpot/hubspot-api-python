"""
    Transactional Email

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.marketing.transactional.configuration import Configuration


class SmtpApiTokenRequestEgg:
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
    openapi_types = {"create_contact": "bool", "campaign_name": "str"}

    attribute_map = {"create_contact": "createContact", "campaign_name": "campaignName"}

    def __init__(
        self, create_contact=None, campaign_name=None, local_vars_configuration=None
    ):  # noqa: E501
        """SmtpApiTokenRequestEgg - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._create_contact = None
        self._campaign_name = None
        self.discriminator = None

        self.create_contact = create_contact
        self.campaign_name = campaign_name

    @property
    def create_contact(self):
        """Gets the create_contact of this SmtpApiTokenRequestEgg.  # noqa: E501

        Indicates whether a contact should be created for recipients of emails.  # noqa: E501

        :return: The create_contact of this SmtpApiTokenRequestEgg.  # noqa: E501
        :rtype: bool
        """
        return self._create_contact

    @create_contact.setter
    def create_contact(self, create_contact):
        """Sets the create_contact of this SmtpApiTokenRequestEgg.

        Indicates whether a contact should be created for recipients of emails.  # noqa: E501

        :param create_contact: The create_contact of this SmtpApiTokenRequestEgg.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation
            and create_contact is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `create_contact`, must not be `None`"
            )  # noqa: E501

        self._create_contact = create_contact

    @property
    def campaign_name(self):
        """Gets the campaign_name of this SmtpApiTokenRequestEgg.  # noqa: E501

        A name for the campaign tied to the SMTP API token.  # noqa: E501

        :return: The campaign_name of this SmtpApiTokenRequestEgg.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this SmtpApiTokenRequestEgg.

        A name for the campaign tied to the SMTP API token.  # noqa: E501

        :param campaign_name: The campaign_name of this SmtpApiTokenRequestEgg.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and campaign_name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `campaign_name`, must not be `None`"
            )  # noqa: E501

        self._campaign_name = campaign_name

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
        if not isinstance(other, SmtpApiTokenRequestEgg):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SmtpApiTokenRequestEgg):
            return True

        return self.to_dict() != other.to_dict()
