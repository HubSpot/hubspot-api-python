# coding: utf-8

"""
    Cms Content Audit

    Use this endpoint to query audit logs of CMS changes that occurred on your HubSpot account.  # noqa: E501

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
    openapi_types = {"meta": "object", "object_name": "str", "full_name": "str", "event": "str", "user_id": "str", "object_id": "str", "object_type": "str", "timestamp": "datetime"}

    attribute_map = {
        "meta": "meta",
        "object_name": "objectName",
        "full_name": "fullName",
        "event": "event",
        "user_id": "userId",
        "object_id": "objectId",
        "object_type": "objectType",
        "timestamp": "timestamp",
    }

    def __init__(self, meta=None, object_name=None, full_name=None, event=None, user_id=None, object_id=None, object_type=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """PublicAuditLog - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._meta = None
        self._object_name = None
        self._full_name = None
        self._event = None
        self._user_id = None
        self._object_id = None
        self._object_type = None
        self._timestamp = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.object_name = object_name
        self.full_name = full_name
        self.event = event
        self.user_id = user_id
        self.object_id = object_id
        self.object_type = object_type
        self.timestamp = timestamp

    @property
    def meta(self):
        """Gets the meta of this PublicAuditLog.  # noqa: E501


        :return: The meta of this PublicAuditLog.  # noqa: E501
        :rtype: object
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this PublicAuditLog.


        :param meta: The meta of this PublicAuditLog.  # noqa: E501
        :type meta: object
        """

        self._meta = meta

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
        :type object_name: str
        """
        if self.local_vars_configuration.client_side_validation and object_name is None:  # noqa: E501
            raise ValueError("Invalid value for `object_name`, must not be `None`")  # noqa: E501

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
        :type full_name: str
        """
        if self.local_vars_configuration.client_side_validation and full_name is None:  # noqa: E501
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

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
        :type event: str
        """
        if self.local_vars_configuration.client_side_validation and event is None:  # noqa: E501
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501
        allowed_values = ["CREATED", "UPDATED", "PUBLISHED", "DELETED", "UNPUBLISHED", "RESTORE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and event not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `event` ({0}), must be one of {1}".format(event, allowed_values))  # noqa: E501

        self._event = event

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
        :type user_id: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

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
        :type object_id: str
        """
        if self.local_vars_configuration.client_side_validation and object_id is None:  # noqa: E501
            raise ValueError("Invalid value for `object_id`, must not be `None`")  # noqa: E501

        self._object_id = object_id

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
        :type object_type: str
        """
        if self.local_vars_configuration.client_side_validation and object_type is None:  # noqa: E501
            raise ValueError("Invalid value for `object_type`, must not be `None`")  # noqa: E501
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
            "CTA",
            "FILE",
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and object_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `object_type` ({0}), must be one of {1}".format(object_type, allowed_values))  # noqa: E501

        self._object_type = object_type

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
        :type timestamp: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

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
        if not isinstance(other, PublicAuditLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicAuditLog):
            return True

        return self.to_dict() != other.to_dict()
