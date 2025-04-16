# coding: utf-8

"""
    Feedback Submissions

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

from hubspot.crm.objects.feedback_submissions.configuration import Configuration


class PublicObjectSearchRequest(object):
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
    openapi_types = {"query": "str", "limit": "int", "after": "str", "sorts": "list[str]", "properties": "list[str]", "filter_groups": "list[FilterGroup]"}

    attribute_map = {"query": "query", "limit": "limit", "after": "after", "sorts": "sorts", "properties": "properties", "filter_groups": "filterGroups"}

    def __init__(self, query=None, limit=None, after=None, sorts=None, properties=None, filter_groups=None, local_vars_configuration=None):  # noqa: E501
        """PublicObjectSearchRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._query = None
        self._limit = None
        self._after = None
        self._sorts = None
        self._properties = None
        self._filter_groups = None
        self.discriminator = None

        if query is not None:
            self.query = query
        if limit is not None:
            self.limit = limit
        if after is not None:
            self.after = after
        if sorts is not None:
            self.sorts = sorts
        if properties is not None:
            self.properties = properties
        if filter_groups is not None:
            self.filter_groups = filter_groups

    @property
    def query(self):
        """Gets the query of this PublicObjectSearchRequest.  # noqa: E501


        :return: The query of this PublicObjectSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this PublicObjectSearchRequest.


        :param query: The query of this PublicObjectSearchRequest.  # noqa: E501
        :type query: str
        """

        self._query = query

    @property
    def limit(self):
        """Gets the limit of this PublicObjectSearchRequest.  # noqa: E501


        :return: The limit of this PublicObjectSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PublicObjectSearchRequest.


        :param limit: The limit of this PublicObjectSearchRequest.  # noqa: E501
        :type limit: int
        """

        self._limit = limit

    @property
    def after(self):
        """Gets the after of this PublicObjectSearchRequest.  # noqa: E501


        :return: The after of this PublicObjectSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """Sets the after of this PublicObjectSearchRequest.


        :param after: The after of this PublicObjectSearchRequest.  # noqa: E501
        :type after: str
        """

        self._after = after

    @property
    def sorts(self):
        """Gets the sorts of this PublicObjectSearchRequest.  # noqa: E501


        :return: The sorts of this PublicObjectSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._sorts

    @sorts.setter
    def sorts(self, sorts):
        """Sets the sorts of this PublicObjectSearchRequest.


        :param sorts: The sorts of this PublicObjectSearchRequest.  # noqa: E501
        :type sorts: list[str]
        """

        self._sorts = sorts

    @property
    def properties(self):
        """Gets the properties of this PublicObjectSearchRequest.  # noqa: E501


        :return: The properties of this PublicObjectSearchRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PublicObjectSearchRequest.


        :param properties: The properties of this PublicObjectSearchRequest.  # noqa: E501
        :type properties: list[str]
        """

        self._properties = properties

    @property
    def filter_groups(self):
        """Gets the filter_groups of this PublicObjectSearchRequest.  # noqa: E501


        :return: The filter_groups of this PublicObjectSearchRequest.  # noqa: E501
        :rtype: list[FilterGroup]
        """
        return self._filter_groups

    @filter_groups.setter
    def filter_groups(self, filter_groups):
        """Sets the filter_groups of this PublicObjectSearchRequest.


        :param filter_groups: The filter_groups of this PublicObjectSearchRequest.  # noqa: E501
        :type filter_groups: list[FilterGroup]
        """

        self._filter_groups = filter_groups

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
        if not isinstance(other, PublicObjectSearchRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicObjectSearchRequest):
            return True

        return self.to_dict() != other.to_dict()
