# coding: utf-8

"""
    Files

    Upload and manage files.  # noqa: E501

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

from hubspot.files.configuration import Configuration


class File(object):
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
        "extension": "str",
        "access": "str",
        "parent_folder_id": "str",
        "source_group": "str",
        "file_md5": "str",
        "encoding": "str",
        "type": "str",
        "is_usable_in_content": "bool",
        "url": "str",
        "expires_at": "int",
        "created_at": "datetime",
        "archived_at": "datetime",
        "path": "str",
        "archived": "bool",
        "size": "int",
        "name": "str",
        "width": "int",
        "id": "str",
        "default_hosting_url": "str",
        "updated_at": "datetime",
        "height": "int",
    }

    attribute_map = {
        "extension": "extension",
        "access": "access",
        "parent_folder_id": "parentFolderId",
        "source_group": "sourceGroup",
        "file_md5": "fileMd5",
        "encoding": "encoding",
        "type": "type",
        "is_usable_in_content": "isUsableInContent",
        "url": "url",
        "expires_at": "expiresAt",
        "created_at": "createdAt",
        "archived_at": "archivedAt",
        "path": "path",
        "archived": "archived",
        "size": "size",
        "name": "name",
        "width": "width",
        "id": "id",
        "default_hosting_url": "defaultHostingUrl",
        "updated_at": "updatedAt",
        "height": "height",
    }

    def __init__(
        self,
        extension=None,
        access=None,
        parent_folder_id=None,
        source_group=None,
        file_md5=None,
        encoding=None,
        type=None,
        is_usable_in_content=None,
        url=None,
        expires_at=None,
        created_at=None,
        archived_at=None,
        path=None,
        archived=None,
        size=None,
        name=None,
        width=None,
        id=None,
        default_hosting_url=None,
        updated_at=None,
        height=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """File - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._extension = None
        self._access = None
        self._parent_folder_id = None
        self._source_group = None
        self._file_md5 = None
        self._encoding = None
        self._type = None
        self._is_usable_in_content = None
        self._url = None
        self._expires_at = None
        self._created_at = None
        self._archived_at = None
        self._path = None
        self._archived = None
        self._size = None
        self._name = None
        self._width = None
        self._id = None
        self._default_hosting_url = None
        self._updated_at = None
        self._height = None
        self.discriminator = None

        if extension is not None:
            self.extension = extension
        self.access = access
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if source_group is not None:
            self.source_group = source_group
        if file_md5 is not None:
            self.file_md5 = file_md5
        if encoding is not None:
            self.encoding = encoding
        if type is not None:
            self.type = type
        if is_usable_in_content is not None:
            self.is_usable_in_content = is_usable_in_content
        if url is not None:
            self.url = url
        if expires_at is not None:
            self.expires_at = expires_at
        self.created_at = created_at
        if archived_at is not None:
            self.archived_at = archived_at
        if path is not None:
            self.path = path
        self.archived = archived
        if size is not None:
            self.size = size
        if name is not None:
            self.name = name
        if width is not None:
            self.width = width
        self.id = id
        if default_hosting_url is not None:
            self.default_hosting_url = default_hosting_url
        self.updated_at = updated_at
        if height is not None:
            self.height = height

    @property
    def extension(self):
        """Gets the extension of this File.  # noqa: E501

        Extension of the file. ex: .jpg, .png, .gif, .pdf, etc.  # noqa: E501

        :return: The extension of this File.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this File.

        Extension of the file. ex: .jpg, .png, .gif, .pdf, etc.  # noqa: E501

        :param extension: The extension of this File.  # noqa: E501
        :type extension: str
        """

        self._extension = extension

    @property
    def access(self):
        """Gets the access of this File.  # noqa: E501

        File access. Can be PUBLIC_INDEXABLE, PUBLIC_NOT_INDEXABLE, PRIVATE.  # noqa: E501

        :return: The access of this File.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this File.

        File access. Can be PUBLIC_INDEXABLE, PUBLIC_NOT_INDEXABLE, PRIVATE.  # noqa: E501

        :param access: The access of this File.  # noqa: E501
        :type access: str
        """
        if self.local_vars_configuration.client_side_validation and access is None:  # noqa: E501
            raise ValueError("Invalid value for `access`, must not be `None`")  # noqa: E501
        allowed_values = ["PUBLIC_INDEXABLE", "PUBLIC_NOT_INDEXABLE", "HIDDEN_INDEXABLE", "HIDDEN_NOT_INDEXABLE", "HIDDEN_PRIVATE", "PRIVATE", "HIDDEN_SENSITIVE", "SENSITIVE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and access not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `access` ({0}), must be one of {1}".format(access, allowed_values))  # noqa: E501

        self._access = access

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this File.  # noqa: E501

        ID of the folder the file is in.  # noqa: E501

        :return: The parent_folder_id of this File.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this File.

        ID of the folder the file is in.  # noqa: E501

        :param parent_folder_id: The parent_folder_id of this File.  # noqa: E501
        :type parent_folder_id: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def source_group(self):
        """Gets the source_group of this File.  # noqa: E501


        :return: The source_group of this File.  # noqa: E501
        :rtype: str
        """
        return self._source_group

    @source_group.setter
    def source_group(self, source_group):
        """Sets the source_group of this File.


        :param source_group: The source_group of this File.  # noqa: E501
        :type source_group: str
        """

        self._source_group = source_group

    @property
    def file_md5(self):
        """Gets the file_md5 of this File.  # noqa: E501


        :return: The file_md5 of this File.  # noqa: E501
        :rtype: str
        """
        return self._file_md5

    @file_md5.setter
    def file_md5(self, file_md5):
        """Sets the file_md5 of this File.


        :param file_md5: The file_md5 of this File.  # noqa: E501
        :type file_md5: str
        """

        self._file_md5 = file_md5

    @property
    def encoding(self):
        """Gets the encoding of this File.  # noqa: E501

        Encoding of the file.  # noqa: E501

        :return: The encoding of this File.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this File.

        Encoding of the file.  # noqa: E501

        :param encoding: The encoding of this File.  # noqa: E501
        :type encoding: str
        """

        self._encoding = encoding

    @property
    def type(self):
        """Gets the type of this File.  # noqa: E501

        Type of the file. Can be IMG, DOCUMENT, AUDIO, MOVIE, or OTHER.  # noqa: E501

        :return: The type of this File.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this File.

        Type of the file. Can be IMG, DOCUMENT, AUDIO, MOVIE, or OTHER.  # noqa: E501

        :param type: The type of this File.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def is_usable_in_content(self):
        """Gets the is_usable_in_content of this File.  # noqa: E501

        Previously \"archied\". Indicates if the file should be used when creating new content like web pages.  # noqa: E501

        :return: The is_usable_in_content of this File.  # noqa: E501
        :rtype: bool
        """
        return self._is_usable_in_content

    @is_usable_in_content.setter
    def is_usable_in_content(self, is_usable_in_content):
        """Sets the is_usable_in_content of this File.

        Previously \"archied\". Indicates if the file should be used when creating new content like web pages.  # noqa: E501

        :param is_usable_in_content: The is_usable_in_content of this File.  # noqa: E501
        :type is_usable_in_content: bool
        """

        self._is_usable_in_content = is_usable_in_content

    @property
    def url(self):
        """Gets the url of this File.  # noqa: E501

        URL of the given file. This URL can change depending on the domain settings of the account. Will use the select file hosting domain.  # noqa: E501

        :return: The url of this File.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this File.

        URL of the given file. This URL can change depending on the domain settings of the account. Will use the select file hosting domain.  # noqa: E501

        :param url: The url of this File.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def expires_at(self):
        """Gets the expires_at of this File.  # noqa: E501


        :return: The expires_at of this File.  # noqa: E501
        :rtype: int
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this File.


        :param expires_at: The expires_at of this File.  # noqa: E501
        :type expires_at: int
        """

        self._expires_at = expires_at

    @property
    def created_at(self):
        """Gets the created_at of this File.  # noqa: E501

        Creation time of the file object.  # noqa: E501

        :return: The created_at of this File.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this File.

        Creation time of the file object.  # noqa: E501

        :param created_at: The created_at of this File.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def archived_at(self):
        """Gets the archived_at of this File.  # noqa: E501

        Deletion time of the file object.  # noqa: E501

        :return: The archived_at of this File.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this File.

        Deletion time of the file object.  # noqa: E501

        :param archived_at: The archived_at of this File.  # noqa: E501
        :type archived_at: datetime
        """

        self._archived_at = archived_at

    @property
    def path(self):
        """Gets the path of this File.  # noqa: E501

        Path of the file in the file manager.  # noqa: E501

        :return: The path of this File.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this File.

        Path of the file in the file manager.  # noqa: E501

        :param path: The path of this File.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def archived(self):
        """Gets the archived of this File.  # noqa: E501

        If the file is deleted.  # noqa: E501

        :return: The archived of this File.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this File.

        If the file is deleted.  # noqa: E501

        :param archived: The archived of this File.  # noqa: E501
        :type archived: bool
        """
        if self.local_vars_configuration.client_side_validation and archived is None:  # noqa: E501
            raise ValueError("Invalid value for `archived`, must not be `None`")  # noqa: E501

        self._archived = archived

    @property
    def size(self):
        """Gets the size of this File.  # noqa: E501

        Size of the file in bytes.  # noqa: E501

        :return: The size of this File.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this File.

        Size of the file in bytes.  # noqa: E501

        :param size: The size of this File.  # noqa: E501
        :type size: int
        """

        self._size = size

    @property
    def name(self):
        """Gets the name of this File.  # noqa: E501

        Name of the file.  # noqa: E501

        :return: The name of this File.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this File.

        Name of the file.  # noqa: E501

        :param name: The name of this File.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def width(self):
        """Gets the width of this File.  # noqa: E501

        For image and video files, the width of the content.  # noqa: E501

        :return: The width of this File.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this File.

        For image and video files, the width of the content.  # noqa: E501

        :param width: The width of this File.  # noqa: E501
        :type width: int
        """

        self._width = width

    @property
    def id(self):
        """Gets the id of this File.  # noqa: E501

        File ID.  # noqa: E501

        :return: The id of this File.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this File.

        File ID.  # noqa: E501

        :param id: The id of this File.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def default_hosting_url(self):
        """Gets the default_hosting_url of this File.  # noqa: E501

        Default hosting URL of the file. This will use one of HubSpot's provided URLs to serve the file.  # noqa: E501

        :return: The default_hosting_url of this File.  # noqa: E501
        :rtype: str
        """
        return self._default_hosting_url

    @default_hosting_url.setter
    def default_hosting_url(self, default_hosting_url):
        """Sets the default_hosting_url of this File.

        Default hosting URL of the file. This will use one of HubSpot's provided URLs to serve the file.  # noqa: E501

        :param default_hosting_url: The default_hosting_url of this File.  # noqa: E501
        :type default_hosting_url: str
        """

        self._default_hosting_url = default_hosting_url

    @property
    def updated_at(self):
        """Gets the updated_at of this File.  # noqa: E501

        Timestamp of the latest update to the file.  # noqa: E501

        :return: The updated_at of this File.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this File.

        Timestamp of the latest update to the file.  # noqa: E501

        :param updated_at: The updated_at of this File.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def height(self):
        """Gets the height of this File.  # noqa: E501

        For image and video files, the height of the content.  # noqa: E501

        :return: The height of this File.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this File.

        For image and video files, the height of the content.  # noqa: E501

        :param height: The height of this File.  # noqa: E501
        :type height: int
        """

        self._height = height

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
        if not isinstance(other, File):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, File):
            return True

        return self.to_dict() != other.to_dict()
