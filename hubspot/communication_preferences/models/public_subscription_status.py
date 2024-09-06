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


class PublicSubscriptionStatus(object):
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
        "brand_id": "int",
        "name": "str",
        "description": "str",
        "legal_basis": "str",
        "preference_group_name": "str",
        "id": "str",
        "legal_basis_explanation": "str",
        "status": "str",
        "source_of_status": "str",
    }

    attribute_map = {
        "brand_id": "brandId",
        "name": "name",
        "description": "description",
        "legal_basis": "legalBasis",
        "preference_group_name": "preferenceGroupName",
        "id": "id",
        "legal_basis_explanation": "legalBasisExplanation",
        "status": "status",
        "source_of_status": "sourceOfStatus",
    }

    def __init__(
        self,
        brand_id=None,
        name=None,
        description=None,
        legal_basis=None,
        preference_group_name=None,
        id=None,
        legal_basis_explanation=None,
        status=None,
        source_of_status=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """PublicSubscriptionStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._brand_id = None
        self._name = None
        self._description = None
        self._legal_basis = None
        self._preference_group_name = None
        self._id = None
        self._legal_basis_explanation = None
        self._status = None
        self._source_of_status = None
        self.discriminator = None

        if brand_id is not None:
            self.brand_id = brand_id
        self.name = name
        self.description = description
        if legal_basis is not None:
            self.legal_basis = legal_basis
        if preference_group_name is not None:
            self.preference_group_name = preference_group_name
        self.id = id
        if legal_basis_explanation is not None:
            self.legal_basis_explanation = legal_basis_explanation
        self.status = status
        self.source_of_status = source_of_status

    @property
    def brand_id(self):
        """Gets the brand_id of this PublicSubscriptionStatus.  # noqa: E501

        The ID of the brand that the subscription is associated with, if there is one.  # noqa: E501

        :return: The brand_id of this PublicSubscriptionStatus.  # noqa: E501
        :rtype: int
        """
        return self._brand_id

    @brand_id.setter
    def brand_id(self, brand_id):
        """Sets the brand_id of this PublicSubscriptionStatus.

        The ID of the brand that the subscription is associated with, if there is one.  # noqa: E501

        :param brand_id: The brand_id of this PublicSubscriptionStatus.  # noqa: E501
        :type brand_id: int
        """

        self._brand_id = brand_id

    @property
    def name(self):
        """Gets the name of this PublicSubscriptionStatus.  # noqa: E501

        The name of the subscription.  # noqa: E501

        :return: The name of this PublicSubscriptionStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PublicSubscriptionStatus.

        The name of the subscription.  # noqa: E501

        :param name: The name of this PublicSubscriptionStatus.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this PublicSubscriptionStatus.  # noqa: E501

        A description of the subscription.  # noqa: E501

        :return: The description of this PublicSubscriptionStatus.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PublicSubscriptionStatus.

        A description of the subscription.  # noqa: E501

        :param description: The description of this PublicSubscriptionStatus.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def legal_basis(self):
        """Gets the legal_basis of this PublicSubscriptionStatus.  # noqa: E501

        The legal reason for the current status of the subscription.  # noqa: E501

        :return: The legal_basis of this PublicSubscriptionStatus.  # noqa: E501
        :rtype: str
        """
        return self._legal_basis

    @legal_basis.setter
    def legal_basis(self, legal_basis):
        """Sets the legal_basis of this PublicSubscriptionStatus.

        The legal reason for the current status of the subscription.  # noqa: E501

        :param legal_basis: The legal_basis of this PublicSubscriptionStatus.  # noqa: E501
        :type legal_basis: str
        """
        allowed_values = [
            "LEGITIMATE_INTEREST_PQL",
            "LEGITIMATE_INTEREST_CLIENT",
            "PERFORMANCE_OF_CONTRACT",
            "CONSENT_WITH_NOTICE",
            "NON_GDPR",
            "PROCESS_AND_STORE",
            "LEGITIMATE_INTEREST_OTHER",
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and legal_basis not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `legal_basis` ({0}), must be one of {1}".format(legal_basis, allowed_values))  # noqa: E501

        self._legal_basis = legal_basis

    @property
    def preference_group_name(self):
        """Gets the preference_group_name of this PublicSubscriptionStatus.  # noqa: E501

        The name of the preferences group that the subscription is associated with.  # noqa: E501

        :return: The preference_group_name of this PublicSubscriptionStatus.  # noqa: E501
        :rtype: str
        """
        return self._preference_group_name

    @preference_group_name.setter
    def preference_group_name(self, preference_group_name):
        """Sets the preference_group_name of this PublicSubscriptionStatus.

        The name of the preferences group that the subscription is associated with.  # noqa: E501

        :param preference_group_name: The preference_group_name of this PublicSubscriptionStatus.  # noqa: E501
        :type preference_group_name: str
        """

        self._preference_group_name = preference_group_name

    @property
    def id(self):
        """Gets the id of this PublicSubscriptionStatus.  # noqa: E501

        The ID for the subscription.  # noqa: E501

        :return: The id of this PublicSubscriptionStatus.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicSubscriptionStatus.

        The ID for the subscription.  # noqa: E501

        :param id: The id of this PublicSubscriptionStatus.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def legal_basis_explanation(self):
        """Gets the legal_basis_explanation of this PublicSubscriptionStatus.  # noqa: E501

        A more detailed explanation to go with the legal basis.  # noqa: E501

        :return: The legal_basis_explanation of this PublicSubscriptionStatus.  # noqa: E501
        :rtype: str
        """
        return self._legal_basis_explanation

    @legal_basis_explanation.setter
    def legal_basis_explanation(self, legal_basis_explanation):
        """Sets the legal_basis_explanation of this PublicSubscriptionStatus.

        A more detailed explanation to go with the legal basis.  # noqa: E501

        :param legal_basis_explanation: The legal_basis_explanation of this PublicSubscriptionStatus.  # noqa: E501
        :type legal_basis_explanation: str
        """

        self._legal_basis_explanation = legal_basis_explanation

    @property
    def status(self):
        """Gets the status of this PublicSubscriptionStatus.  # noqa: E501

        Whether the contact is subscribed.  # noqa: E501

        :return: The status of this PublicSubscriptionStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PublicSubscriptionStatus.

        Whether the contact is subscribed.  # noqa: E501

        :param status: The status of this PublicSubscriptionStatus.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["SUBSCRIBED", "NOT_SUBSCRIBED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `status` ({0}), must be one of {1}".format(status, allowed_values))  # noqa: E501

        self._status = status

    @property
    def source_of_status(self):
        """Gets the source_of_status of this PublicSubscriptionStatus.  # noqa: E501

        Where the status is determined from e.g. PORTAL_WIDE_STATUS if the contact opted out from the portal.  # noqa: E501

        :return: The source_of_status of this PublicSubscriptionStatus.  # noqa: E501
        :rtype: str
        """
        return self._source_of_status

    @source_of_status.setter
    def source_of_status(self, source_of_status):
        """Sets the source_of_status of this PublicSubscriptionStatus.

        Where the status is determined from e.g. PORTAL_WIDE_STATUS if the contact opted out from the portal.  # noqa: E501

        :param source_of_status: The source_of_status of this PublicSubscriptionStatus.  # noqa: E501
        :type source_of_status: str
        """
        if self.local_vars_configuration.client_side_validation and source_of_status is None:  # noqa: E501
            raise ValueError("Invalid value for `source_of_status`, must not be `None`")  # noqa: E501
        allowed_values = ["PORTAL_WIDE_STATUS", "BRAND_WIDE_STATUS", "SUBSCRIPTION_STATUS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and source_of_status not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `source_of_status` ({0}), must be one of {1}".format(source_of_status, allowed_values))  # noqa: E501

        self._source_of_status = source_of_status

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
        if not isinstance(other, PublicSubscriptionStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicSubscriptionStatus):
            return True

        return self.to_dict() != other.to_dict()
