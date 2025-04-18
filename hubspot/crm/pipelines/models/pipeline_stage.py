# coding: utf-8

"""
    Pipelines

    Pipelines represent distinct stages in a workflow, like closing a deal or servicing a support ticket. These endpoints provide access to read and modify pipelines in HubSpot. Pipelines support `deals` and `tickets` object types.  ## Pipeline ID validation  When calling endpoints that take pipelineId as a parameter, that ID must correspond to an existing, un-archived pipeline. Otherwise the request will fail with a `404 Not Found` response.  # noqa: E501

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

from hubspot.crm.pipelines.configuration import Configuration


class PipelineStage(object):
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
        "created_at": "datetime",
        "archived_at": "datetime",
        "archived": "bool",
        "metadata": "dict[str, str]",
        "display_order": "int",
        "write_permissions": "str",
        "label": "str",
        "id": "str",
        "updated_at": "datetime",
    }

    attribute_map = {
        "created_at": "createdAt",
        "archived_at": "archivedAt",
        "archived": "archived",
        "metadata": "metadata",
        "display_order": "displayOrder",
        "write_permissions": "writePermissions",
        "label": "label",
        "id": "id",
        "updated_at": "updatedAt",
    }

    def __init__(
        self, created_at=None, archived_at=None, archived=None, metadata=None, display_order=None, write_permissions=None, label=None, id=None, updated_at=None, local_vars_configuration=None
    ):  # noqa: E501
        """PipelineStage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._archived_at = None
        self._archived = None
        self._metadata = None
        self._display_order = None
        self._write_permissions = None
        self._label = None
        self._id = None
        self._updated_at = None
        self.discriminator = None

        self.created_at = created_at
        if archived_at is not None:
            self.archived_at = archived_at
        self.archived = archived
        if metadata is not None:
            self.metadata = metadata
        self.display_order = display_order
        if write_permissions is not None:
            self.write_permissions = write_permissions
        self.label = label
        self.id = id
        self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this PipelineStage.  # noqa: E501

        The date the pipeline stage was created. The stages on default pipelines will have createdAt = 0.  # noqa: E501

        :return: The created_at of this PipelineStage.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PipelineStage.

        The date the pipeline stage was created. The stages on default pipelines will have createdAt = 0.  # noqa: E501

        :param created_at: The created_at of this PipelineStage.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def archived_at(self):
        """Gets the archived_at of this PipelineStage.  # noqa: E501

        The date the pipeline was archived. `archivedAt` will only be present if the pipeline is archived.  # noqa: E501

        :return: The archived_at of this PipelineStage.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this PipelineStage.

        The date the pipeline was archived. `archivedAt` will only be present if the pipeline is archived.  # noqa: E501

        :param archived_at: The archived_at of this PipelineStage.  # noqa: E501
        :type archived_at: datetime
        """

        self._archived_at = archived_at

    @property
    def archived(self):
        """Gets the archived of this PipelineStage.  # noqa: E501

        Whether the pipeline is archived.  # noqa: E501

        :return: The archived of this PipelineStage.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this PipelineStage.

        Whether the pipeline is archived.  # noqa: E501

        :param archived: The archived of this PipelineStage.  # noqa: E501
        :type archived: bool
        """
        if self.local_vars_configuration.client_side_validation and archived is None:  # noqa: E501
            raise ValueError("Invalid value for `archived`, must not be `None`")  # noqa: E501

        self._archived = archived

    @property
    def metadata(self):
        """Gets the metadata of this PipelineStage.  # noqa: E501

        A JSON object containing properties that are not present on all object pipelines.  For `deals` pipelines, the `probability` field is required (`{ \"probability\": 0.5 }`), and represents the likelihood a deal will close. Possible values are between 0.0 and 1.0 in increments of 0.1.  For `tickets` pipelines, the `ticketState` field is optional (`{ \"ticketState\": \"OPEN\" }`), and represents whether the ticket remains open or has been closed by a member of your Support team. Possible values are `OPEN` or `CLOSED`.  # noqa: E501

        :return: The metadata of this PipelineStage.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PipelineStage.

        A JSON object containing properties that are not present on all object pipelines.  For `deals` pipelines, the `probability` field is required (`{ \"probability\": 0.5 }`), and represents the likelihood a deal will close. Possible values are between 0.0 and 1.0 in increments of 0.1.  For `tickets` pipelines, the `ticketState` field is optional (`{ \"ticketState\": \"OPEN\" }`), and represents whether the ticket remains open or has been closed by a member of your Support team. Possible values are `OPEN` or `CLOSED`.  # noqa: E501

        :param metadata: The metadata of this PipelineStage.  # noqa: E501
        :type metadata: dict[str, str]
        """

        self._metadata = metadata

    @property
    def display_order(self):
        """Gets the display_order of this PipelineStage.  # noqa: E501

        The order for displaying this pipeline stage. If two pipeline stages have a matching `displayOrder`, they will be sorted alphabetically by label.  # noqa: E501

        :return: The display_order of this PipelineStage.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this PipelineStage.

        The order for displaying this pipeline stage. If two pipeline stages have a matching `displayOrder`, they will be sorted alphabetically by label.  # noqa: E501

        :param display_order: The display_order of this PipelineStage.  # noqa: E501
        :type display_order: int
        """
        if self.local_vars_configuration.client_side_validation and display_order is None:  # noqa: E501
            raise ValueError("Invalid value for `display_order`, must not be `None`")  # noqa: E501

        self._display_order = display_order

    @property
    def write_permissions(self):
        """Gets the write_permissions of this PipelineStage.  # noqa: E501


        :return: The write_permissions of this PipelineStage.  # noqa: E501
        :rtype: str
        """
        return self._write_permissions

    @write_permissions.setter
    def write_permissions(self, write_permissions):
        """Sets the write_permissions of this PipelineStage.


        :param write_permissions: The write_permissions of this PipelineStage.  # noqa: E501
        :type write_permissions: str
        """
        allowed_values = ["CRM_PERMISSIONS_ENFORCEMENT", "READ_ONLY", "INTERNAL_ONLY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and write_permissions not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `write_permissions` ({0}), must be one of {1}".format(write_permissions, allowed_values))  # noqa: E501

        self._write_permissions = write_permissions

    @property
    def label(self):
        """Gets the label of this PipelineStage.  # noqa: E501

        A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's label must be unique within that pipeline.  # noqa: E501

        :return: The label of this PipelineStage.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PipelineStage.

        A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's label must be unique within that pipeline.  # noqa: E501

        :param label: The label of this PipelineStage.  # noqa: E501
        :type label: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def id(self):
        """Gets the id of this PipelineStage.  # noqa: E501

        A unique identifier generated by HubSpot that can be used to retrieve and update the pipeline stage.  # noqa: E501

        :return: The id of this PipelineStage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PipelineStage.

        A unique identifier generated by HubSpot that can be used to retrieve and update the pipeline stage.  # noqa: E501

        :param id: The id of this PipelineStage.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def updated_at(self):
        """Gets the updated_at of this PipelineStage.  # noqa: E501

        The date the pipeline stage was last updated.  # noqa: E501

        :return: The updated_at of this PipelineStage.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PipelineStage.

        The date the pipeline stage was last updated.  # noqa: E501

        :param updated_at: The updated_at of this PipelineStage.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, PipelineStage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineStage):
            return True

        return self.to_dict() != other.to_dict()
