# coding: utf-8

"""
    Schemas

    The CRM uses schemas to define how custom objects should store and represent information in the HubSpot CRM. Schemas define details about an object's type, properties, and associations. The schema can be uniquely identified by its **object type ID**.  # noqa: E501

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

from hubspot.crm.schemas.configuration import Configuration


class ModelProperty(object):
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
        "hidden": "bool",
        "display_order": "int",
        "description": "str",
        "show_currency_symbol": "bool",
        "type": "str",
        "hubspot_defined": "bool",
        "created_at": "datetime",
        "archived": "bool",
        "options": "list[Option]",
        "has_unique_value": "bool",
        "calculated": "bool",
        "external_options": "bool",
        "updated_at": "datetime",
        "created_user_id": "str",
        "modification_metadata": "PropertyModificationMetadata",
        "sensitive_data_categories": "list[str]",
        "label": "str",
        "form_field": "bool",
        "data_sensitivity": "str",
        "archived_at": "datetime",
        "group_name": "str",
        "referenced_object_type": "str",
        "name": "str",
        "calculation_formula": "str",
        "field_type": "str",
        "updated_user_id": "str",
    }

    attribute_map = {
        "hidden": "hidden",
        "display_order": "displayOrder",
        "description": "description",
        "show_currency_symbol": "showCurrencySymbol",
        "type": "type",
        "hubspot_defined": "hubspotDefined",
        "created_at": "createdAt",
        "archived": "archived",
        "options": "options",
        "has_unique_value": "hasUniqueValue",
        "calculated": "calculated",
        "external_options": "externalOptions",
        "updated_at": "updatedAt",
        "created_user_id": "createdUserId",
        "modification_metadata": "modificationMetadata",
        "sensitive_data_categories": "sensitiveDataCategories",
        "label": "label",
        "form_field": "formField",
        "data_sensitivity": "dataSensitivity",
        "archived_at": "archivedAt",
        "group_name": "groupName",
        "referenced_object_type": "referencedObjectType",
        "name": "name",
        "calculation_formula": "calculationFormula",
        "field_type": "fieldType",
        "updated_user_id": "updatedUserId",
    }

    def __init__(
        self,
        hidden=None,
        display_order=None,
        description=None,
        show_currency_symbol=None,
        type=None,
        hubspot_defined=None,
        created_at=None,
        archived=None,
        options=None,
        has_unique_value=None,
        calculated=None,
        external_options=None,
        updated_at=None,
        created_user_id=None,
        modification_metadata=None,
        sensitive_data_categories=None,
        label=None,
        form_field=None,
        data_sensitivity=None,
        archived_at=None,
        group_name=None,
        referenced_object_type=None,
        name=None,
        calculation_formula=None,
        field_type=None,
        updated_user_id=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """ModelProperty - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._hidden = None
        self._display_order = None
        self._description = None
        self._show_currency_symbol = None
        self._type = None
        self._hubspot_defined = None
        self._created_at = None
        self._archived = None
        self._options = None
        self._has_unique_value = None
        self._calculated = None
        self._external_options = None
        self._updated_at = None
        self._created_user_id = None
        self._modification_metadata = None
        self._sensitive_data_categories = None
        self._label = None
        self._form_field = None
        self._data_sensitivity = None
        self._archived_at = None
        self._group_name = None
        self._referenced_object_type = None
        self._name = None
        self._calculation_formula = None
        self._field_type = None
        self._updated_user_id = None
        self.discriminator = None

        if hidden is not None:
            self.hidden = hidden
        if display_order is not None:
            self.display_order = display_order
        self.description = description
        if show_currency_symbol is not None:
            self.show_currency_symbol = show_currency_symbol
        self.type = type
        if hubspot_defined is not None:
            self.hubspot_defined = hubspot_defined
        if created_at is not None:
            self.created_at = created_at
        if archived is not None:
            self.archived = archived
        self.options = options
        if has_unique_value is not None:
            self.has_unique_value = has_unique_value
        if calculated is not None:
            self.calculated = calculated
        if external_options is not None:
            self.external_options = external_options
        if updated_at is not None:
            self.updated_at = updated_at
        if created_user_id is not None:
            self.created_user_id = created_user_id
        if modification_metadata is not None:
            self.modification_metadata = modification_metadata
        if sensitive_data_categories is not None:
            self.sensitive_data_categories = sensitive_data_categories
        self.label = label
        if form_field is not None:
            self.form_field = form_field
        if data_sensitivity is not None:
            self.data_sensitivity = data_sensitivity
        if archived_at is not None:
            self.archived_at = archived_at
        self.group_name = group_name
        if referenced_object_type is not None:
            self.referenced_object_type = referenced_object_type
        self.name = name
        if calculation_formula is not None:
            self.calculation_formula = calculation_formula
        self.field_type = field_type
        if updated_user_id is not None:
            self.updated_user_id = updated_user_id

    @property
    def hidden(self):
        """Gets the hidden of this ModelProperty.  # noqa: E501


        :return: The hidden of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this ModelProperty.


        :param hidden: The hidden of this ModelProperty.  # noqa: E501
        :type hidden: bool
        """

        self._hidden = hidden

    @property
    def display_order(self):
        """Gets the display_order of this ModelProperty.  # noqa: E501

        The order that this property should be displayed in the HubSpot UI relative to other properties for this object type. Properties are displayed in order starting with the lowest positive integer value. A value of -1 will cause the property to be displayed **after** any positive values.  # noqa: E501

        :return: The display_order of this ModelProperty.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this ModelProperty.

        The order that this property should be displayed in the HubSpot UI relative to other properties for this object type. Properties are displayed in order starting with the lowest positive integer value. A value of -1 will cause the property to be displayed **after** any positive values.  # noqa: E501

        :param display_order: The display_order of this ModelProperty.  # noqa: E501
        :type display_order: int
        """

        self._display_order = display_order

    @property
    def description(self):
        """Gets the description of this ModelProperty.  # noqa: E501

        A description of the property that will be shown as help text in HubSpot.  # noqa: E501

        :return: The description of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelProperty.

        A description of the property that will be shown as help text in HubSpot.  # noqa: E501

        :param description: The description of this ModelProperty.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def show_currency_symbol(self):
        """Gets the show_currency_symbol of this ModelProperty.  # noqa: E501

        Whether the property will display the currency symbol set in the account settings.  # noqa: E501

        :return: The show_currency_symbol of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._show_currency_symbol

    @show_currency_symbol.setter
    def show_currency_symbol(self, show_currency_symbol):
        """Sets the show_currency_symbol of this ModelProperty.

        Whether the property will display the currency symbol set in the account settings.  # noqa: E501

        :param show_currency_symbol: The show_currency_symbol of this ModelProperty.  # noqa: E501
        :type show_currency_symbol: bool
        """

        self._show_currency_symbol = show_currency_symbol

    @property
    def type(self):
        """Gets the type of this ModelProperty.  # noqa: E501

        The property data type.  # noqa: E501

        :return: The type of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelProperty.

        The property data type.  # noqa: E501

        :param type: The type of this ModelProperty.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def hubspot_defined(self):
        """Gets the hubspot_defined of this ModelProperty.  # noqa: E501

        This will be true for default object properties built into HubSpot.  # noqa: E501

        :return: The hubspot_defined of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._hubspot_defined

    @hubspot_defined.setter
    def hubspot_defined(self, hubspot_defined):
        """Sets the hubspot_defined of this ModelProperty.

        This will be true for default object properties built into HubSpot.  # noqa: E501

        :param hubspot_defined: The hubspot_defined of this ModelProperty.  # noqa: E501
        :type hubspot_defined: bool
        """

        self._hubspot_defined = hubspot_defined

    @property
    def created_at(self):
        """Gets the created_at of this ModelProperty.  # noqa: E501

        When the property was created  # noqa: E501

        :return: The created_at of this ModelProperty.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelProperty.

        When the property was created  # noqa: E501

        :param created_at: The created_at of this ModelProperty.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def archived(self):
        """Gets the archived of this ModelProperty.  # noqa: E501

        Whether or not the property is archived.  # noqa: E501

        :return: The archived of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this ModelProperty.

        Whether or not the property is archived.  # noqa: E501

        :param archived: The archived of this ModelProperty.  # noqa: E501
        :type archived: bool
        """

        self._archived = archived

    @property
    def options(self):
        """Gets the options of this ModelProperty.  # noqa: E501

        A list of valid options for the property. This field is required for enumerated properties, but will be empty for other property types.  # noqa: E501

        :return: The options of this ModelProperty.  # noqa: E501
        :rtype: list[Option]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ModelProperty.

        A list of valid options for the property. This field is required for enumerated properties, but will be empty for other property types.  # noqa: E501

        :param options: The options of this ModelProperty.  # noqa: E501
        :type options: list[Option]
        """
        if self.local_vars_configuration.client_side_validation and options is None:  # noqa: E501
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def has_unique_value(self):
        """Gets the has_unique_value of this ModelProperty.  # noqa: E501

        Whether or not the property's value must be unique. Once set, this can't be changed.  # noqa: E501

        :return: The has_unique_value of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._has_unique_value

    @has_unique_value.setter
    def has_unique_value(self, has_unique_value):
        """Sets the has_unique_value of this ModelProperty.

        Whether or not the property's value must be unique. Once set, this can't be changed.  # noqa: E501

        :param has_unique_value: The has_unique_value of this ModelProperty.  # noqa: E501
        :type has_unique_value: bool
        """

        self._has_unique_value = has_unique_value

    @property
    def calculated(self):
        """Gets the calculated of this ModelProperty.  # noqa: E501

        For default properties, true indicates that the property is calculated by a HubSpot process. It has no effect for custom properties.  # noqa: E501

        :return: The calculated of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._calculated

    @calculated.setter
    def calculated(self, calculated):
        """Sets the calculated of this ModelProperty.

        For default properties, true indicates that the property is calculated by a HubSpot process. It has no effect for custom properties.  # noqa: E501

        :param calculated: The calculated of this ModelProperty.  # noqa: E501
        :type calculated: bool
        """

        self._calculated = calculated

    @property
    def external_options(self):
        """Gets the external_options of this ModelProperty.  # noqa: E501

        For default properties, true indicates that the options are stored externally to the property settings.  # noqa: E501

        :return: The external_options of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._external_options

    @external_options.setter
    def external_options(self, external_options):
        """Sets the external_options of this ModelProperty.

        For default properties, true indicates that the options are stored externally to the property settings.  # noqa: E501

        :param external_options: The external_options of this ModelProperty.  # noqa: E501
        :type external_options: bool
        """

        self._external_options = external_options

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelProperty.  # noqa: E501

          # noqa: E501

        :return: The updated_at of this ModelProperty.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelProperty.

          # noqa: E501

        :param updated_at: The updated_at of this ModelProperty.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def created_user_id(self):
        """Gets the created_user_id of this ModelProperty.  # noqa: E501

        The internal ID of the user who created the property in HubSpot. This field may not exist if the property was created outside of HubSpot.  # noqa: E501

        :return: The created_user_id of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._created_user_id

    @created_user_id.setter
    def created_user_id(self, created_user_id):
        """Sets the created_user_id of this ModelProperty.

        The internal ID of the user who created the property in HubSpot. This field may not exist if the property was created outside of HubSpot.  # noqa: E501

        :param created_user_id: The created_user_id of this ModelProperty.  # noqa: E501
        :type created_user_id: str
        """

        self._created_user_id = created_user_id

    @property
    def modification_metadata(self):
        """Gets the modification_metadata of this ModelProperty.  # noqa: E501


        :return: The modification_metadata of this ModelProperty.  # noqa: E501
        :rtype: PropertyModificationMetadata
        """
        return self._modification_metadata

    @modification_metadata.setter
    def modification_metadata(self, modification_metadata):
        """Sets the modification_metadata of this ModelProperty.


        :param modification_metadata: The modification_metadata of this ModelProperty.  # noqa: E501
        :type modification_metadata: PropertyModificationMetadata
        """

        self._modification_metadata = modification_metadata

    @property
    def sensitive_data_categories(self):
        """Gets the sensitive_data_categories of this ModelProperty.  # noqa: E501


        :return: The sensitive_data_categories of this ModelProperty.  # noqa: E501
        :rtype: list[str]
        """
        return self._sensitive_data_categories

    @sensitive_data_categories.setter
    def sensitive_data_categories(self, sensitive_data_categories):
        """Sets the sensitive_data_categories of this ModelProperty.


        :param sensitive_data_categories: The sensitive_data_categories of this ModelProperty.  # noqa: E501
        :type sensitive_data_categories: list[str]
        """

        self._sensitive_data_categories = sensitive_data_categories

    @property
    def label(self):
        """Gets the label of this ModelProperty.  # noqa: E501

        A human-readable property label that will be shown in HubSpot.  # noqa: E501

        :return: The label of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ModelProperty.

        A human-readable property label that will be shown in HubSpot.  # noqa: E501

        :param label: The label of this ModelProperty.  # noqa: E501
        :type label: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def form_field(self):
        """Gets the form_field of this ModelProperty.  # noqa: E501

        Whether or not the property can be used in a HubSpot form.  # noqa: E501

        :return: The form_field of this ModelProperty.  # noqa: E501
        :rtype: bool
        """
        return self._form_field

    @form_field.setter
    def form_field(self, form_field):
        """Sets the form_field of this ModelProperty.

        Whether or not the property can be used in a HubSpot form.  # noqa: E501

        :param form_field: The form_field of this ModelProperty.  # noqa: E501
        :type form_field: bool
        """

        self._form_field = form_field

    @property
    def data_sensitivity(self):
        """Gets the data_sensitivity of this ModelProperty.  # noqa: E501


        :return: The data_sensitivity of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._data_sensitivity

    @data_sensitivity.setter
    def data_sensitivity(self, data_sensitivity):
        """Sets the data_sensitivity of this ModelProperty.


        :param data_sensitivity: The data_sensitivity of this ModelProperty.  # noqa: E501
        :type data_sensitivity: str
        """
        allowed_values = ["non_sensitive", "sensitive", "highly_sensitive"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and data_sensitivity not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `data_sensitivity` ({0}), must be one of {1}".format(data_sensitivity, allowed_values))  # noqa: E501

        self._data_sensitivity = data_sensitivity

    @property
    def archived_at(self):
        """Gets the archived_at of this ModelProperty.  # noqa: E501

        When the property was archived.  # noqa: E501

        :return: The archived_at of this ModelProperty.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this ModelProperty.

        When the property was archived.  # noqa: E501

        :param archived_at: The archived_at of this ModelProperty.  # noqa: E501
        :type archived_at: datetime
        """

        self._archived_at = archived_at

    @property
    def group_name(self):
        """Gets the group_name of this ModelProperty.  # noqa: E501

        The name of the property group the property belongs to.  # noqa: E501

        :return: The group_name of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ModelProperty.

        The name of the property group the property belongs to.  # noqa: E501

        :param group_name: The group_name of this ModelProperty.  # noqa: E501
        :type group_name: str
        """
        if self.local_vars_configuration.client_side_validation and group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def referenced_object_type(self):
        """Gets the referenced_object_type of this ModelProperty.  # noqa: E501

        If this property is related to other object(s), they'll be listed here.  # noqa: E501

        :return: The referenced_object_type of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._referenced_object_type

    @referenced_object_type.setter
    def referenced_object_type(self, referenced_object_type):
        """Sets the referenced_object_type of this ModelProperty.

        If this property is related to other object(s), they'll be listed here.  # noqa: E501

        :param referenced_object_type: The referenced_object_type of this ModelProperty.  # noqa: E501
        :type referenced_object_type: str
        """

        self._referenced_object_type = referenced_object_type

    @property
    def name(self):
        """Gets the name of this ModelProperty.  # noqa: E501

        The internal property name, which must be used when referencing the property via the API.  # noqa: E501

        :return: The name of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelProperty.

        The internal property name, which must be used when referencing the property via the API.  # noqa: E501

        :param name: The name of this ModelProperty.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def calculation_formula(self):
        """Gets the calculation_formula of this ModelProperty.  # noqa: E501


        :return: The calculation_formula of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._calculation_formula

    @calculation_formula.setter
    def calculation_formula(self, calculation_formula):
        """Sets the calculation_formula of this ModelProperty.


        :param calculation_formula: The calculation_formula of this ModelProperty.  # noqa: E501
        :type calculation_formula: str
        """

        self._calculation_formula = calculation_formula

    @property
    def field_type(self):
        """Gets the field_type of this ModelProperty.  # noqa: E501

        Controls how the property appears in HubSpot.  # noqa: E501

        :return: The field_type of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this ModelProperty.

        Controls how the property appears in HubSpot.  # noqa: E501

        :param field_type: The field_type of this ModelProperty.  # noqa: E501
        :type field_type: str
        """
        if self.local_vars_configuration.client_side_validation and field_type is None:  # noqa: E501
            raise ValueError("Invalid value for `field_type`, must not be `None`")  # noqa: E501

        self._field_type = field_type

    @property
    def updated_user_id(self):
        """Gets the updated_user_id of this ModelProperty.  # noqa: E501

        The internal user ID of the user who updated the property in HubSpot. This field may not exist if the property was updated outside of HubSpot.  # noqa: E501

        :return: The updated_user_id of this ModelProperty.  # noqa: E501
        :rtype: str
        """
        return self._updated_user_id

    @updated_user_id.setter
    def updated_user_id(self, updated_user_id):
        """Sets the updated_user_id of this ModelProperty.

        The internal user ID of the user who updated the property in HubSpot. This field may not exist if the property was updated outside of HubSpot.  # noqa: E501

        :param updated_user_id: The updated_user_id of this ModelProperty.  # noqa: E501
        :type updated_user_id: str
        """

        self._updated_user_id = updated_user_id

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
        if not isinstance(other, ModelProperty):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelProperty):
            return True

        return self.to_dict() != other.to_dict()
