# coding: utf-8

"""
    CRM Objects

    CRM objects such as companies, contacts, deals, line items, products, tickets, and quotes are standard objects in HubSpot’s CRM. These core building blocks support custom properties, store critical information, and play a central role in the HubSpot application.  ## Supported Object Types  This API provides access to collections of CRM objects, which return a map of property names to values. Each object type has its own set of default properties, which can be found by exploring the [CRM Object Properties API](https://developers.hubspot.com/docs/methods/crm-properties/crm-properties-overview).  |Object Type |Properties returned by default | |--|--| | `companies` | `name`, `domain` | | `contacts` | `firstname`, `lastname`, `email` | | `deals` | `dealname`, `amount`, `closedate`, `pipeline`, `dealstage` | | `products` | `name`, `description`, `price` | | `tickets` | `content`, `hs_pipeline`, `hs_pipeline_stage`, `hs_ticket_category`, `hs_ticket_priority`, `subject` |  Find a list of all properties for an object type using the [CRM Object Properties](https://developers.hubspot.com/docs/methods/crm-properties/get-properties) API. e.g. `GET https://api.hubapi.com/properties/v2/companies/properties`. Change the properties returned in the response using the `properties` array in the request body.  # noqa: E501

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

from hubspot.crm.objects.configuration import Configuration


class SimplePublicObjectInputForCreate(object):
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
    openapi_types = {"associations": "list[PublicAssociationsForObject]", "properties": "dict[str, str]"}

    attribute_map = {"associations": "associations", "properties": "properties"}

    def __init__(self, associations=None, properties=None, local_vars_configuration=None):  # noqa: E501
        """SimplePublicObjectInputForCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._associations = None
        self._properties = None
        self.discriminator = None

        if associations is not None:
            self.associations = associations
        self.properties = properties

    @property
    def associations(self):
        """Gets the associations of this SimplePublicObjectInputForCreate.  # noqa: E501


        :return: The associations of this SimplePublicObjectInputForCreate.  # noqa: E501
        :rtype: list[PublicAssociationsForObject]
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Sets the associations of this SimplePublicObjectInputForCreate.


        :param associations: The associations of this SimplePublicObjectInputForCreate.  # noqa: E501
        :type associations: list[PublicAssociationsForObject]
        """

        self._associations = associations

    @property
    def properties(self):
        """Gets the properties of this SimplePublicObjectInputForCreate.  # noqa: E501


        :return: The properties of this SimplePublicObjectInputForCreate.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SimplePublicObjectInputForCreate.


        :param properties: The properties of this SimplePublicObjectInputForCreate.  # noqa: E501
        :type properties: dict[str, str]
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

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
        if not isinstance(other, SimplePublicObjectInputForCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimplePublicObjectInputForCreate):
            return True

        return self.to_dict() != other.to_dict()
