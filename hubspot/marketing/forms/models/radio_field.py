# coding: utf-8

"""
    Forms

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

from hubspot.marketing.forms.configuration import Configuration


class RadioField(object):
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
        "object_type_id": "str",
        "hidden": "bool",
        "name": "str",
        "options": "list[EnumeratedFieldOption]",
        "description": "str",
        "default_values": "list[str]",
        "dependent_fields": "list[DependentField]",
        "label": "str",
        "placeholder": "str",
        "field_type": "str",
        "required": "bool",
    }

    attribute_map = {
        "object_type_id": "objectTypeId",
        "hidden": "hidden",
        "name": "name",
        "options": "options",
        "description": "description",
        "default_values": "defaultValues",
        "dependent_fields": "dependentFields",
        "label": "label",
        "placeholder": "placeholder",
        "field_type": "fieldType",
        "required": "required",
    }

    def __init__(
        self,
        object_type_id=None,
        hidden=None,
        name=None,
        options=None,
        description=None,
        default_values=None,
        dependent_fields=None,
        label=None,
        placeholder=None,
        field_type="radio",
        required=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """RadioField - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._object_type_id = None
        self._hidden = None
        self._name = None
        self._options = None
        self._description = None
        self._default_values = None
        self._dependent_fields = None
        self._label = None
        self._placeholder = None
        self._field_type = None
        self._required = None
        self.discriminator = None

        self.object_type_id = object_type_id
        self.hidden = hidden
        self.name = name
        self.options = options
        if description is not None:
            self.description = description
        self.default_values = default_values
        self.dependent_fields = dependent_fields
        self.label = label
        if placeholder is not None:
            self.placeholder = placeholder
        self.field_type = field_type
        self.required = required

    @property
    def object_type_id(self):
        """Gets the object_type_id of this RadioField.  # noqa: E501

        A unique ID for this field's CRM object type. For example a CONTACT field will have the object type ID 0-1.  # noqa: E501

        :return: The object_type_id of this RadioField.  # noqa: E501
        :rtype: str
        """
        return self._object_type_id

    @object_type_id.setter
    def object_type_id(self, object_type_id):
        """Sets the object_type_id of this RadioField.

        A unique ID for this field's CRM object type. For example a CONTACT field will have the object type ID 0-1.  # noqa: E501

        :param object_type_id: The object_type_id of this RadioField.  # noqa: E501
        :type object_type_id: str
        """
        if self.local_vars_configuration.client_side_validation and object_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `object_type_id`, must not be `None`")  # noqa: E501

        self._object_type_id = object_type_id

    @property
    def hidden(self):
        """Gets the hidden of this RadioField.  # noqa: E501

        Whether a field should be hidden or not. Hidden fields won't appear on the form, but can be used to pass a value to a property without requiring the customer to fill it in.  # noqa: E501

        :return: The hidden of this RadioField.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this RadioField.

        Whether a field should be hidden or not. Hidden fields won't appear on the form, but can be used to pass a value to a property without requiring the customer to fill it in.  # noqa: E501

        :param hidden: The hidden of this RadioField.  # noqa: E501
        :type hidden: bool
        """
        if self.local_vars_configuration.client_side_validation and hidden is None:  # noqa: E501
            raise ValueError("Invalid value for `hidden`, must not be `None`")  # noqa: E501

        self._hidden = hidden

    @property
    def name(self):
        """Gets the name of this RadioField.  # noqa: E501

        The identifier of the field. In combination with the object type ID, it must be unique.  # noqa: E501

        :return: The name of this RadioField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RadioField.

        The identifier of the field. In combination with the object type ID, it must be unique.  # noqa: E501

        :param name: The name of this RadioField.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def options(self):
        """Gets the options of this RadioField.  # noqa: E501

        The list of available choices for this field.  # noqa: E501

        :return: The options of this RadioField.  # noqa: E501
        :rtype: list[EnumeratedFieldOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this RadioField.

        The list of available choices for this field.  # noqa: E501

        :param options: The options of this RadioField.  # noqa: E501
        :type options: list[EnumeratedFieldOption]
        """
        if self.local_vars_configuration.client_side_validation and options is None:  # noqa: E501
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def description(self):
        """Gets the description of this RadioField.  # noqa: E501

        Additional text helping the customer to complete the field.  # noqa: E501

        :return: The description of this RadioField.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RadioField.

        Additional text helping the customer to complete the field.  # noqa: E501

        :param description: The description of this RadioField.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def default_values(self):
        """Gets the default_values of this RadioField.  # noqa: E501

        The values selected by default. Those values will be submitted unless the customer modifies them.  # noqa: E501

        :return: The default_values of this RadioField.  # noqa: E501
        :rtype: list[str]
        """
        return self._default_values

    @default_values.setter
    def default_values(self, default_values):
        """Sets the default_values of this RadioField.

        The values selected by default. Those values will be submitted unless the customer modifies them.  # noqa: E501

        :param default_values: The default_values of this RadioField.  # noqa: E501
        :type default_values: list[str]
        """
        if self.local_vars_configuration.client_side_validation and default_values is None:  # noqa: E501
            raise ValueError("Invalid value for `default_values`, must not be `None`")  # noqa: E501

        self._default_values = default_values

    @property
    def dependent_fields(self):
        """Gets the dependent_fields of this RadioField.  # noqa: E501

        A list of other fields to make visible based on the value filled in for this field.  # noqa: E501

        :return: The dependent_fields of this RadioField.  # noqa: E501
        :rtype: list[DependentField]
        """
        return self._dependent_fields

    @dependent_fields.setter
    def dependent_fields(self, dependent_fields):
        """Sets the dependent_fields of this RadioField.

        A list of other fields to make visible based on the value filled in for this field.  # noqa: E501

        :param dependent_fields: The dependent_fields of this RadioField.  # noqa: E501
        :type dependent_fields: list[DependentField]
        """
        if self.local_vars_configuration.client_side_validation and dependent_fields is None:  # noqa: E501
            raise ValueError("Invalid value for `dependent_fields`, must not be `None`")  # noqa: E501

        self._dependent_fields = dependent_fields

    @property
    def label(self):
        """Gets the label of this RadioField.  # noqa: E501

        The main label for the form field.  # noqa: E501

        :return: The label of this RadioField.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this RadioField.

        The main label for the form field.  # noqa: E501

        :param label: The label of this RadioField.  # noqa: E501
        :type label: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def placeholder(self):
        """Gets the placeholder of this RadioField.  # noqa: E501

        The prompt text showing when the field isn't filled in.  # noqa: E501

        :return: The placeholder of this RadioField.  # noqa: E501
        :rtype: str
        """
        return self._placeholder

    @placeholder.setter
    def placeholder(self, placeholder):
        """Sets the placeholder of this RadioField.

        The prompt text showing when the field isn't filled in.  # noqa: E501

        :param placeholder: The placeholder of this RadioField.  # noqa: E501
        :type placeholder: str
        """

        self._placeholder = placeholder

    @property
    def field_type(self):
        """Gets the field_type of this RadioField.  # noqa: E501

        Determines how the field will be displayed and validated.  # noqa: E501

        :return: The field_type of this RadioField.  # noqa: E501
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this RadioField.

        Determines how the field will be displayed and validated.  # noqa: E501

        :param field_type: The field_type of this RadioField.  # noqa: E501
        :type field_type: str
        """
        if self.local_vars_configuration.client_side_validation and field_type is None:  # noqa: E501
            raise ValueError("Invalid value for `field_type`, must not be `None`")  # noqa: E501
        allowed_values = ["radio"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and field_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `field_type` ({0}), must be one of {1}".format(field_type, allowed_values))  # noqa: E501

        self._field_type = field_type

    @property
    def required(self):
        """Gets the required of this RadioField.  # noqa: E501

        Whether a value for this field is required when submitting the form.  # noqa: E501

        :return: The required of this RadioField.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this RadioField.

        Whether a value for this field is required when submitting the form.  # noqa: E501

        :param required: The required of this RadioField.  # noqa: E501
        :type required: bool
        """
        if self.local_vars_configuration.client_side_validation and required is None:  # noqa: E501
            raise ValueError("Invalid value for `required`, must not be `None`")  # noqa: E501

        self._required = required

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
        if not isinstance(other, RadioField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RadioField):
            return True

        return self.to_dict() != other.to_dict()
