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


class HubDbTableCloneRequest(object):
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
    openapi_types = {"new_name": "str", "is_hubspot_defined": "bool", "new_label": "str", "copy_rows": "bool"}

    attribute_map = {"new_name": "newName", "is_hubspot_defined": "isHubspotDefined", "new_label": "newLabel", "copy_rows": "copyRows"}

    def __init__(self, new_name=None, is_hubspot_defined=None, new_label=None, copy_rows=None, local_vars_configuration=None):  # noqa: E501
        """HubDbTableCloneRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._new_name = None
        self._is_hubspot_defined = None
        self._new_label = None
        self._copy_rows = None
        self.discriminator = None

        if new_name is not None:
            self.new_name = new_name
        self.is_hubspot_defined = is_hubspot_defined
        if new_label is not None:
            self.new_label = new_label
        self.copy_rows = copy_rows

    @property
    def new_name(self):
        """Gets the new_name of this HubDbTableCloneRequest.  # noqa: E501

        The new name for the cloned table  # noqa: E501

        :return: The new_name of this HubDbTableCloneRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this HubDbTableCloneRequest.

        The new name for the cloned table  # noqa: E501

        :param new_name: The new_name of this HubDbTableCloneRequest.  # noqa: E501
        :type new_name: str
        """

        self._new_name = new_name

    @property
    def is_hubspot_defined(self):
        """Gets the is_hubspot_defined of this HubDbTableCloneRequest.  # noqa: E501


        :return: The is_hubspot_defined of this HubDbTableCloneRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_hubspot_defined

    @is_hubspot_defined.setter
    def is_hubspot_defined(self, is_hubspot_defined):
        """Sets the is_hubspot_defined of this HubDbTableCloneRequest.


        :param is_hubspot_defined: The is_hubspot_defined of this HubDbTableCloneRequest.  # noqa: E501
        :type is_hubspot_defined: bool
        """
        if self.local_vars_configuration.client_side_validation and is_hubspot_defined is None:  # noqa: E501
            raise ValueError("Invalid value for `is_hubspot_defined`, must not be `None`")  # noqa: E501

        self._is_hubspot_defined = is_hubspot_defined

    @property
    def new_label(self):
        """Gets the new_label of this HubDbTableCloneRequest.  # noqa: E501

        The new label for the cloned table  # noqa: E501

        :return: The new_label of this HubDbTableCloneRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_label

    @new_label.setter
    def new_label(self, new_label):
        """Sets the new_label of this HubDbTableCloneRequest.

        The new label for the cloned table  # noqa: E501

        :param new_label: The new_label of this HubDbTableCloneRequest.  # noqa: E501
        :type new_label: str
        """

        self._new_label = new_label

    @property
    def copy_rows(self):
        """Gets the copy_rows of this HubDbTableCloneRequest.  # noqa: E501

        Specifies whether to copy the rows during clone  # noqa: E501

        :return: The copy_rows of this HubDbTableCloneRequest.  # noqa: E501
        :rtype: bool
        """
        return self._copy_rows

    @copy_rows.setter
    def copy_rows(self, copy_rows):
        """Sets the copy_rows of this HubDbTableCloneRequest.

        Specifies whether to copy the rows during clone  # noqa: E501

        :param copy_rows: The copy_rows of this HubDbTableCloneRequest.  # noqa: E501
        :type copy_rows: bool
        """
        if self.local_vars_configuration.client_side_validation and copy_rows is None:  # noqa: E501
            raise ValueError("Invalid value for `copy_rows`, must not be `None`")  # noqa: E501

        self._copy_rows = copy_rows

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
        if not isinstance(other, HubDbTableCloneRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HubDbTableCloneRequest):
            return True

        return self.to_dict() != other.to_dict()
