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


class ListFolderCreateRequest(object):
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
    openapi_types = {"parent_folder_id": "str", "name": "str"}

    attribute_map = {"parent_folder_id": "parentFolderId", "name": "name"}

    def __init__(self, parent_folder_id=None, name=None, local_vars_configuration=None):  # noqa: E501
        """ListFolderCreateRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._parent_folder_id = None
        self._name = None
        self.discriminator = None

        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        self.name = name

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this ListFolderCreateRequest.  # noqa: E501

        The folder this should be created in, if not specified will be created in the root folder 0.  # noqa: E501

        :return: The parent_folder_id of this ListFolderCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this ListFolderCreateRequest.

        The folder this should be created in, if not specified will be created in the root folder 0.  # noqa: E501

        :param parent_folder_id: The parent_folder_id of this ListFolderCreateRequest.  # noqa: E501
        :type parent_folder_id: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def name(self):
        """Gets the name of this ListFolderCreateRequest.  # noqa: E501

        The name of the folder to be created.  # noqa: E501

        :return: The name of this ListFolderCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListFolderCreateRequest.

        The name of the folder to be created.  # noqa: E501

        :param name: The name of this ListFolderCreateRequest.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, ListFolderCreateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListFolderCreateRequest):
            return True

        return self.to_dict() != other.to_dict()
