# coding: utf-8

"""
    Lists

    CRUD operations to manage lists and list memberships  # noqa: E501

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


class PublicInListFilter(object):
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
    openapi_types = {"filter_type": "str", "list_id": "int", "metadata": "PublicInListFilterMetadata", "operator": "str"}

    attribute_map = {"filter_type": "filterType", "list_id": "listId", "metadata": "metadata", "operator": "operator"}

    def __init__(self, filter_type="IN_LIST", list_id=None, metadata=None, operator=None, local_vars_configuration=None):  # noqa: E501
        """PublicInListFilter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._filter_type = None
        self._list_id = None
        self._metadata = None
        self._operator = None
        self.discriminator = None

        self.filter_type = filter_type
        self.list_id = list_id
        if metadata is not None:
            self.metadata = metadata
        self.operator = operator

    @property
    def filter_type(self):
        """Gets the filter_type of this PublicInListFilter.  # noqa: E501


        :return: The filter_type of this PublicInListFilter.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this PublicInListFilter.


        :param filter_type: The filter_type of this PublicInListFilter.  # noqa: E501
        :type filter_type: str
        """
        if self.local_vars_configuration.client_side_validation and filter_type is None:  # noqa: E501
            raise ValueError("Invalid value for `filter_type`, must not be `None`")  # noqa: E501
        allowed_values = ["IN_LIST"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and filter_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `filter_type` ({0}), must be one of {1}".format(filter_type, allowed_values))  # noqa: E501

        self._filter_type = filter_type

    @property
    def list_id(self):
        """Gets the list_id of this PublicInListFilter.  # noqa: E501


        :return: The list_id of this PublicInListFilter.  # noqa: E501
        :rtype: int
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this PublicInListFilter.


        :param list_id: The list_id of this PublicInListFilter.  # noqa: E501
        :type list_id: int
        """
        if self.local_vars_configuration.client_side_validation and list_id is None:  # noqa: E501
            raise ValueError("Invalid value for `list_id`, must not be `None`")  # noqa: E501

        self._list_id = list_id

    @property
    def metadata(self):
        """Gets the metadata of this PublicInListFilter.  # noqa: E501


        :return: The metadata of this PublicInListFilter.  # noqa: E501
        :rtype: PublicInListFilterMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PublicInListFilter.


        :param metadata: The metadata of this PublicInListFilter.  # noqa: E501
        :type metadata: PublicInListFilterMetadata
        """

        self._metadata = metadata

    @property
    def operator(self):
        """Gets the operator of this PublicInListFilter.  # noqa: E501


        :return: The operator of this PublicInListFilter.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PublicInListFilter.


        :param operator: The operator of this PublicInListFilter.  # noqa: E501
        :type operator: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

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
        if not isinstance(other, PublicInListFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicInListFilter):
            return True

        return self.to_dict() != other.to_dict()