# coding: utf-8

"""
    CRM Owners

    HubSpot uses **owners** to assign CRM objects to specific people in your organization. The endpoints described here are used to get a list of the owners that are available for an account. To assign an owner to an object, set the hubspot_owner_id property using the appropriate CRM object update or create a request.  If teams are available for your HubSpot tier, these endpoints will also indicate which team an owner belongs to. Team membership can be one of PRIMARY (default), SECONDARY, or CHILD.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.owners.configuration import Configuration


class PublicOwner(object):
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
        "id": "str",
        "email": "str",
        "first_name": "str",
        "last_name": "str",
        "user_id": "int",
        "created_at": "datetime",
        "updated_at": "datetime",
        "archived": "bool",
        "teams": "list[PublicTeam]",
    }

    attribute_map = {
        "id": "id",
        "email": "email",
        "first_name": "firstName",
        "last_name": "lastName",
        "user_id": "userId",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "archived": "archived",
        "teams": "teams",
    }

    def __init__(
        self,
        id=None,
        email=None,
        first_name=None,
        last_name=None,
        user_id=None,
        created_at=None,
        updated_at=None,
        archived=None,
        teams=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """PublicOwner - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._user_id = None
        self._created_at = None
        self._updated_at = None
        self._archived = None
        self._teams = None
        self.discriminator = None

        self.id = id
        if email is not None:
            self.email = email
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if user_id is not None:
            self.user_id = user_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.archived = archived
        if teams is not None:
            self.teams = teams

    @property
    def id(self):
        """Gets the id of this PublicOwner.  # noqa: E501


        :return: The id of this PublicOwner.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicOwner.


        :param id: The id of this PublicOwner.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and id is None
        ):  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email(self):
        """Gets the email of this PublicOwner.  # noqa: E501


        :return: The email of this PublicOwner.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PublicOwner.


        :param email: The email of this PublicOwner.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this PublicOwner.  # noqa: E501


        :return: The first_name of this PublicOwner.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PublicOwner.


        :param first_name: The first_name of this PublicOwner.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this PublicOwner.  # noqa: E501


        :return: The last_name of this PublicOwner.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PublicOwner.


        :param last_name: The last_name of this PublicOwner.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def user_id(self):
        """Gets the user_id of this PublicOwner.  # noqa: E501


        :return: The user_id of this PublicOwner.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PublicOwner.


        :param user_id: The user_id of this PublicOwner.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def created_at(self):
        """Gets the created_at of this PublicOwner.  # noqa: E501


        :return: The created_at of this PublicOwner.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PublicOwner.


        :param created_at: The created_at of this PublicOwner.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation and created_at is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `created_at`, must not be `None`"
            )  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PublicOwner.  # noqa: E501


        :return: The updated_at of this PublicOwner.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PublicOwner.


        :param updated_at: The updated_at of this PublicOwner.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation and updated_at is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `updated_at`, must not be `None`"
            )  # noqa: E501

        self._updated_at = updated_at

    @property
    def archived(self):
        """Gets the archived of this PublicOwner.  # noqa: E501


        :return: The archived of this PublicOwner.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this PublicOwner.


        :param archived: The archived of this PublicOwner.  # noqa: E501
        :type: bool
        """
        if (
            self.local_vars_configuration.client_side_validation and archived is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `archived`, must not be `None`"
            )  # noqa: E501

        self._archived = archived

    @property
    def teams(self):
        """Gets the teams of this PublicOwner.  # noqa: E501


        :return: The teams of this PublicOwner.  # noqa: E501
        :rtype: list[PublicTeam]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this PublicOwner.


        :param teams: The teams of this PublicOwner.  # noqa: E501
        :type: list[PublicTeam]
        """

        self._teams = teams

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, PublicOwner):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicOwner):
            return True

        return self.to_dict() != other.to_dict()
