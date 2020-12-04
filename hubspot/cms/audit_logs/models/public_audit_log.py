# coding: utf-8

"""
    CMS Audit Logs

    Use this endpoint to query audit logs of CMS changes that occurred on your HubSpot account.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.audit_logs.configuration import Configuration


class PublicAuditLog(object):
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
        "object_id": "str",
        "user_id": "str",
        "timestamp": "datetime",
        "object_name": "str",
        "full_name": "str",
        "event": "str",
        "object_type": "str",
    }

    attribute_map = {
        "object_id": "objectId",
        "user_id": "userId",
        "timestamp": "timestamp",
        "object_name": "objectName",
        "full_name": "fullName",
        "event": "event",
        "object_type": "objectType",
    }

    def __init__(
        self,
        object_id=None,
        user_id=None,
        timestamp=None,
        object_name=None,
        full_name=None,
        event=None,
        object_type=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """PublicAuditLog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._object_id = None
        self._user_id = None
        self._timestamp = None
        self._object_name = None
        self._full_name = None
        self._event = None
        self._object_type = None
        self.discriminator = None

        self.object_id = object_id
        self.user_id = user_id
        self.timestamp = timestamp
        self.object_name = object_name
        self.full_name = full_name
        self.event = event
        self.object_type = object_type

    @property
    def object_id(self):
        """Gets the object_id of this PublicAuditLog.  # noqa: E501

        The ID of the object.  # noqa: E501

        :return: The object_id of this PublicAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this PublicAuditLog.

        The ID of the object.  # noqa: E501

        :param object_id: The object_id of this PublicAuditLog.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and object_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `object_id`, must not be `None`"
            )  # noqa: E501

        self._object_id = object_id

    @property
    def user_id(self):
        """Gets the user_id of this PublicAuditLog.  # noqa: E501

        The ID of the user who caused the event.  # noqa: E501

        :return: The user_id of this PublicAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PublicAuditLog.

        The ID of the user who caused the event.  # noqa: E501

        :param user_id: The user_id of this PublicAuditLog.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and user_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `user_id`, must not be `None`"
            )  # noqa: E501

        self._user_id = user_id

    @property
    def timestamp(self):
        """Gets the timestamp of this PublicAuditLog.  # noqa: E501

        The timestamp at which the event occurred.  # noqa: E501

        :return: The timestamp of this PublicAuditLog.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PublicAuditLog.

        The timestamp at which the event occurred.  # noqa: E501

        :param timestamp: The timestamp of this PublicAuditLog.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation and timestamp is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `timestamp`, must not be `None`"
            )  # noqa: E501

        self._timestamp = timestamp

    @property
    def object_name(self):
        """Gets the object_name of this PublicAuditLog.  # noqa: E501

        The internal name of the object in HubSpot.  # noqa: E501

        :return: The object_name of this PublicAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this PublicAuditLog.

        The internal name of the object in HubSpot.  # noqa: E501

        :param object_name: The object_name of this PublicAuditLog.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and object_name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `object_name`, must not be `None`"
            )  # noqa: E501

        self._object_name = object_name

    @property
    def full_name(self):
        """Gets the full_name of this PublicAuditLog.  # noqa: E501

        The name of the user who caused the event.  # noqa: E501

        :return: The full_name of this PublicAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this PublicAuditLog.

        The name of the user who caused the event.  # noqa: E501

        :param full_name: The full_name of this PublicAuditLog.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and full_name is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `full_name`, must not be `None`"
            )  # noqa: E501

        self._full_name = full_name

    @property
    def event(self):
        """Gets the event of this PublicAuditLog.  # noqa: E501

        The type of event that took place (CREATED, UPDATED, PUBLISHED, DELETED, UNPUBLISHED).  # noqa: E501

        :return: The event of this PublicAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this PublicAuditLog.

        The type of event that took place (CREATED, UPDATED, PUBLISHED, DELETED, UNPUBLISHED).  # noqa: E501

        :param event: The event of this PublicAuditLog.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and event is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `event`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "CREATED",
            "UPDATED",
            "PUBLISHED",
            "DELETED",
            "UNPUBLISHED",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and event not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `event` ({0}), must be one of {1}".format(  # noqa: E501
                    event, allowed_values
                )
            )

        self._event = event

    @property
    def object_type(self):
        """Gets the object_type of this PublicAuditLog.  # noqa: E501

        The type of the object (BLOG, LANDING_PAGE, DOMAIN, HUBDB_TABLE etc.)  # noqa: E501

        :return: The object_type of this PublicAuditLog.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this PublicAuditLog.

        The type of the object (BLOG, LANDING_PAGE, DOMAIN, HUBDB_TABLE etc.)  # noqa: E501

        :param object_type: The object_type of this PublicAuditLog.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and object_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `object_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = [
            "BLOG",
            "BLOG_POST",
            "LANDING_PAGE",
            "WEBSITE_PAGE",
            "TEMPLATE",
            "MODULE",
            "GLOBAL_MODULE",
            "SERVERLESS_FUNCTION",
            "DOMAIN",
            "URL_MAPPING",
            "EMAIL",
            "CONTENT_SETTINGS",
            "HUBDB_TABLE",
            "KNOWLEDGE_BASE_ARTICLE",
            "KNOWLEDGE_BASE",
            "THEME",
            "CSS",
            "JS",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and object_type not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `object_type` ({0}), must be one of {1}".format(  # noqa: E501
                    object_type, allowed_values
                )
            )

        self._object_type = object_type

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
        if not isinstance(other, PublicAuditLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicAuditLog):
            return True

        return self.to_dict() != other.to_dict()
