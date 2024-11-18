# coding: utf-8

"""
    CRM Associations Schema

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.crm.associations.v4.schema.configuration import Configuration


class PublicAssociationDefinitionConfigurationUpdateResult(object):
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
    openapi_types = {"user_enforced_max_to_object_ids": "int", "type_id": "int", "category": "str"}

    attribute_map = {"user_enforced_max_to_object_ids": "userEnforcedMaxToObjectIds", "type_id": "typeId", "category": "category"}

    def __init__(self, user_enforced_max_to_object_ids=None, type_id=None, category=None, local_vars_configuration=None):  # noqa: E501
        """PublicAssociationDefinitionConfigurationUpdateResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._user_enforced_max_to_object_ids = None
        self._type_id = None
        self._category = None
        self.discriminator = None

        if user_enforced_max_to_object_ids is not None:
            self.user_enforced_max_to_object_ids = user_enforced_max_to_object_ids
        self.type_id = type_id
        self.category = category

    @property
    def user_enforced_max_to_object_ids(self):
        """Gets the user_enforced_max_to_object_ids of this PublicAssociationDefinitionConfigurationUpdateResult.  # noqa: E501


        :return: The user_enforced_max_to_object_ids of this PublicAssociationDefinitionConfigurationUpdateResult.  # noqa: E501
        :rtype: int
        """
        return self._user_enforced_max_to_object_ids

    @user_enforced_max_to_object_ids.setter
    def user_enforced_max_to_object_ids(self, user_enforced_max_to_object_ids):
        """Sets the user_enforced_max_to_object_ids of this PublicAssociationDefinitionConfigurationUpdateResult.


        :param user_enforced_max_to_object_ids: The user_enforced_max_to_object_ids of this PublicAssociationDefinitionConfigurationUpdateResult.  # noqa: E501
        :type user_enforced_max_to_object_ids: int
        """

        self._user_enforced_max_to_object_ids = user_enforced_max_to_object_ids

    @property
    def type_id(self):
        """Gets the type_id of this PublicAssociationDefinitionConfigurationUpdateResult.  # noqa: E501


        :return: The type_id of this PublicAssociationDefinitionConfigurationUpdateResult.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this PublicAssociationDefinitionConfigurationUpdateResult.


        :param type_id: The type_id of this PublicAssociationDefinitionConfigurationUpdateResult.  # noqa: E501
        :type type_id: int
        """
        if self.local_vars_configuration.client_side_validation and type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def category(self):
        """Gets the category of this PublicAssociationDefinitionConfigurationUpdateResult.  # noqa: E501


        :return: The category of this PublicAssociationDefinitionConfigurationUpdateResult.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this PublicAssociationDefinitionConfigurationUpdateResult.


        :param category: The category of this PublicAssociationDefinitionConfigurationUpdateResult.  # noqa: E501
        :type category: str
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501
        allowed_values = ["HUBSPOT_DEFINED", "USER_DEFINED", "INTEGRATOR_DEFINED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and category not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `category` ({0}), must be one of {1}".format(category, allowed_values))  # noqa: E501

        self._category = category

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
        if not isinstance(other, PublicAssociationDefinitionConfigurationUpdateResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicAssociationDefinitionConfigurationUpdateResult):
            return True

        return self.to_dict() != other.to_dict()
