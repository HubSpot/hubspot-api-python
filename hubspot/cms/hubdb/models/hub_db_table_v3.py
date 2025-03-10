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


class HubDbTableV3(object):
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
        "dynamic_meta_tags": "dict[str, int]",
        "updated_by": "SimpleUser",
        "allow_public_api_access": "bool",
        "use_for_pages": "bool",
        "published_at": "datetime",
        "columns": "list[Column]",
        "label": "str",
        "published": "bool",
        "column_count": "int",
        "allow_child_tables": "bool",
        "created_at": "datetime",
        "deleted": "bool",
        "created_by": "SimpleUser",
        "name": "str",
        "enable_child_table_pages": "bool",
        "id": "str",
        "row_count": "int",
        "is_ordered_manually": "bool",
        "updated_at": "datetime",
    }

    attribute_map = {
        "dynamic_meta_tags": "dynamicMetaTags",
        "updated_by": "updatedBy",
        "allow_public_api_access": "allowPublicApiAccess",
        "use_for_pages": "useForPages",
        "published_at": "publishedAt",
        "columns": "columns",
        "label": "label",
        "published": "published",
        "column_count": "columnCount",
        "allow_child_tables": "allowChildTables",
        "created_at": "createdAt",
        "deleted": "deleted",
        "created_by": "createdBy",
        "name": "name",
        "enable_child_table_pages": "enableChildTablePages",
        "id": "id",
        "row_count": "rowCount",
        "is_ordered_manually": "isOrderedManually",
        "updated_at": "updatedAt",
    }

    def __init__(
        self,
        dynamic_meta_tags=None,
        updated_by=None,
        allow_public_api_access=None,
        use_for_pages=None,
        published_at=None,
        columns=None,
        label=None,
        published=None,
        column_count=None,
        allow_child_tables=None,
        created_at=None,
        deleted=None,
        created_by=None,
        name=None,
        enable_child_table_pages=None,
        id=None,
        row_count=None,
        is_ordered_manually=None,
        updated_at=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """HubDbTableV3 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._dynamic_meta_tags = None
        self._updated_by = None
        self._allow_public_api_access = None
        self._use_for_pages = None
        self._published_at = None
        self._columns = None
        self._label = None
        self._published = None
        self._column_count = None
        self._allow_child_tables = None
        self._created_at = None
        self._deleted = None
        self._created_by = None
        self._name = None
        self._enable_child_table_pages = None
        self._id = None
        self._row_count = None
        self._is_ordered_manually = None
        self._updated_at = None
        self.discriminator = None

        if dynamic_meta_tags is not None:
            self.dynamic_meta_tags = dynamic_meta_tags
        if updated_by is not None:
            self.updated_by = updated_by
        if allow_public_api_access is not None:
            self.allow_public_api_access = allow_public_api_access
        if use_for_pages is not None:
            self.use_for_pages = use_for_pages
        if published_at is not None:
            self.published_at = published_at
        if columns is not None:
            self.columns = columns
        self.label = label
        if published is not None:
            self.published = published
        if column_count is not None:
            self.column_count = column_count
        if allow_child_tables is not None:
            self.allow_child_tables = allow_child_tables
        if created_at is not None:
            self.created_at = created_at
        if deleted is not None:
            self.deleted = deleted
        if created_by is not None:
            self.created_by = created_by
        self.name = name
        if enable_child_table_pages is not None:
            self.enable_child_table_pages = enable_child_table_pages
        if id is not None:
            self.id = id
        if row_count is not None:
            self.row_count = row_count
        if is_ordered_manually is not None:
            self.is_ordered_manually = is_ordered_manually
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def dynamic_meta_tags(self):
        """Gets the dynamic_meta_tags of this HubDbTableV3.  # noqa: E501

        Specifies the key value pairs of the [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages) with the associated column IDs.  # noqa: E501

        :return: The dynamic_meta_tags of this HubDbTableV3.  # noqa: E501
        :rtype: dict[str, int]
        """
        return self._dynamic_meta_tags

    @dynamic_meta_tags.setter
    def dynamic_meta_tags(self, dynamic_meta_tags):
        """Sets the dynamic_meta_tags of this HubDbTableV3.

        Specifies the key value pairs of the [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages) with the associated column IDs.  # noqa: E501

        :param dynamic_meta_tags: The dynamic_meta_tags of this HubDbTableV3.  # noqa: E501
        :type dynamic_meta_tags: dict[str, int]
        """

        self._dynamic_meta_tags = dynamic_meta_tags

    @property
    def updated_by(self):
        """Gets the updated_by of this HubDbTableV3.  # noqa: E501


        :return: The updated_by of this HubDbTableV3.  # noqa: E501
        :rtype: SimpleUser
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this HubDbTableV3.


        :param updated_by: The updated_by of this HubDbTableV3.  # noqa: E501
        :type updated_by: SimpleUser
        """

        self._updated_by = updated_by

    @property
    def allow_public_api_access(self):
        """Gets the allow_public_api_access of this HubDbTableV3.  # noqa: E501

        Specifies whether the table can be read by public without authorization  # noqa: E501

        :return: The allow_public_api_access of this HubDbTableV3.  # noqa: E501
        :rtype: bool
        """
        return self._allow_public_api_access

    @allow_public_api_access.setter
    def allow_public_api_access(self, allow_public_api_access):
        """Sets the allow_public_api_access of this HubDbTableV3.

        Specifies whether the table can be read by public without authorization  # noqa: E501

        :param allow_public_api_access: The allow_public_api_access of this HubDbTableV3.  # noqa: E501
        :type allow_public_api_access: bool
        """

        self._allow_public_api_access = allow_public_api_access

    @property
    def use_for_pages(self):
        """Gets the use_for_pages of this HubDbTableV3.  # noqa: E501

        Specifies whether the table can be used for creation of dynamic pages  # noqa: E501

        :return: The use_for_pages of this HubDbTableV3.  # noqa: E501
        :rtype: bool
        """
        return self._use_for_pages

    @use_for_pages.setter
    def use_for_pages(self, use_for_pages):
        """Sets the use_for_pages of this HubDbTableV3.

        Specifies whether the table can be used for creation of dynamic pages  # noqa: E501

        :param use_for_pages: The use_for_pages of this HubDbTableV3.  # noqa: E501
        :type use_for_pages: bool
        """

        self._use_for_pages = use_for_pages

    @property
    def published_at(self):
        """Gets the published_at of this HubDbTableV3.  # noqa: E501

        Timestamp at which the table is published recently  # noqa: E501

        :return: The published_at of this HubDbTableV3.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at

    @published_at.setter
    def published_at(self, published_at):
        """Sets the published_at of this HubDbTableV3.

        Timestamp at which the table is published recently  # noqa: E501

        :param published_at: The published_at of this HubDbTableV3.  # noqa: E501
        :type published_at: datetime
        """

        self._published_at = published_at

    @property
    def columns(self):
        """Gets the columns of this HubDbTableV3.  # noqa: E501

        List of columns in the table  # noqa: E501

        :return: The columns of this HubDbTableV3.  # noqa: E501
        :rtype: list[Column]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this HubDbTableV3.

        List of columns in the table  # noqa: E501

        :param columns: The columns of this HubDbTableV3.  # noqa: E501
        :type columns: list[Column]
        """

        self._columns = columns

    @property
    def label(self):
        """Gets the label of this HubDbTableV3.  # noqa: E501

        Label of the table  # noqa: E501

        :return: The label of this HubDbTableV3.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this HubDbTableV3.

        Label of the table  # noqa: E501

        :param label: The label of this HubDbTableV3.  # noqa: E501
        :type label: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def published(self):
        """Gets the published of this HubDbTableV3.  # noqa: E501


        :return: The published of this HubDbTableV3.  # noqa: E501
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this HubDbTableV3.


        :param published: The published of this HubDbTableV3.  # noqa: E501
        :type published: bool
        """

        self._published = published

    @property
    def column_count(self):
        """Gets the column_count of this HubDbTableV3.  # noqa: E501

        Number of columns including deleted  # noqa: E501

        :return: The column_count of this HubDbTableV3.  # noqa: E501
        :rtype: int
        """
        return self._column_count

    @column_count.setter
    def column_count(self, column_count):
        """Sets the column_count of this HubDbTableV3.

        Number of columns including deleted  # noqa: E501

        :param column_count: The column_count of this HubDbTableV3.  # noqa: E501
        :type column_count: int
        """

        self._column_count = column_count

    @property
    def allow_child_tables(self):
        """Gets the allow_child_tables of this HubDbTableV3.  # noqa: E501

        Specifies whether child tables can be created  # noqa: E501

        :return: The allow_child_tables of this HubDbTableV3.  # noqa: E501
        :rtype: bool
        """
        return self._allow_child_tables

    @allow_child_tables.setter
    def allow_child_tables(self, allow_child_tables):
        """Sets the allow_child_tables of this HubDbTableV3.

        Specifies whether child tables can be created  # noqa: E501

        :param allow_child_tables: The allow_child_tables of this HubDbTableV3.  # noqa: E501
        :type allow_child_tables: bool
        """

        self._allow_child_tables = allow_child_tables

    @property
    def created_at(self):
        """Gets the created_at of this HubDbTableV3.  # noqa: E501

        Timestamp at which the table is created  # noqa: E501

        :return: The created_at of this HubDbTableV3.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this HubDbTableV3.

        Timestamp at which the table is created  # noqa: E501

        :param created_at: The created_at of this HubDbTableV3.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def deleted(self):
        """Gets the deleted of this HubDbTableV3.  # noqa: E501


        :return: The deleted of this HubDbTableV3.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this HubDbTableV3.


        :param deleted: The deleted of this HubDbTableV3.  # noqa: E501
        :type deleted: bool
        """

        self._deleted = deleted

    @property
    def created_by(self):
        """Gets the created_by of this HubDbTableV3.  # noqa: E501


        :return: The created_by of this HubDbTableV3.  # noqa: E501
        :rtype: SimpleUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this HubDbTableV3.


        :param created_by: The created_by of this HubDbTableV3.  # noqa: E501
        :type created_by: SimpleUser
        """

        self._created_by = created_by

    @property
    def name(self):
        """Gets the name of this HubDbTableV3.  # noqa: E501

        Name of the table  # noqa: E501

        :return: The name of this HubDbTableV3.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HubDbTableV3.

        Name of the table  # noqa: E501

        :param name: The name of this HubDbTableV3.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def enable_child_table_pages(self):
        """Gets the enable_child_table_pages of this HubDbTableV3.  # noqa: E501

        Specifies creation of multi-level dynamic pages using child tables  # noqa: E501

        :return: The enable_child_table_pages of this HubDbTableV3.  # noqa: E501
        :rtype: bool
        """
        return self._enable_child_table_pages

    @enable_child_table_pages.setter
    def enable_child_table_pages(self, enable_child_table_pages):
        """Sets the enable_child_table_pages of this HubDbTableV3.

        Specifies creation of multi-level dynamic pages using child tables  # noqa: E501

        :param enable_child_table_pages: The enable_child_table_pages of this HubDbTableV3.  # noqa: E501
        :type enable_child_table_pages: bool
        """

        self._enable_child_table_pages = enable_child_table_pages

    @property
    def id(self):
        """Gets the id of this HubDbTableV3.  # noqa: E501

        Id of the table  # noqa: E501

        :return: The id of this HubDbTableV3.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HubDbTableV3.

        Id of the table  # noqa: E501

        :param id: The id of this HubDbTableV3.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def row_count(self):
        """Gets the row_count of this HubDbTableV3.  # noqa: E501

        Number of rows in the table  # noqa: E501

        :return: The row_count of this HubDbTableV3.  # noqa: E501
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this HubDbTableV3.

        Number of rows in the table  # noqa: E501

        :param row_count: The row_count of this HubDbTableV3.  # noqa: E501
        :type row_count: int
        """

        self._row_count = row_count

    @property
    def is_ordered_manually(self):
        """Gets the is_ordered_manually of this HubDbTableV3.  # noqa: E501


        :return: The is_ordered_manually of this HubDbTableV3.  # noqa: E501
        :rtype: bool
        """
        return self._is_ordered_manually

    @is_ordered_manually.setter
    def is_ordered_manually(self, is_ordered_manually):
        """Sets the is_ordered_manually of this HubDbTableV3.


        :param is_ordered_manually: The is_ordered_manually of this HubDbTableV3.  # noqa: E501
        :type is_ordered_manually: bool
        """

        self._is_ordered_manually = is_ordered_manually

    @property
    def updated_at(self):
        """Gets the updated_at of this HubDbTableV3.  # noqa: E501

        Timestamp at which the table is updated recently  # noqa: E501

        :return: The updated_at of this HubDbTableV3.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this HubDbTableV3.

        Timestamp at which the table is updated recently  # noqa: E501

        :param updated_at: The updated_at of this HubDbTableV3.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, HubDbTableV3):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HubDbTableV3):
            return True

        return self.to_dict() != other.to_dict()
