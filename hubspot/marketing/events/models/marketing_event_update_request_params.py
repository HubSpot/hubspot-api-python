# coding: utf-8

"""
    Marketing Events

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

from hubspot.marketing.events.configuration import Configuration


class MarketingEventUpdateRequestParams(object):
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
        "start_date_time": "datetime",
        "custom_properties": "list[PropertyValue]",
        "event_cancelled": "bool",
        "event_organizer": "str",
        "event_url": "str",
        "event_description": "str",
        "event_name": "str",
        "event_type": "str",
        "event_completed": "bool",
        "end_date_time": "datetime",
    }

    attribute_map = {
        "start_date_time": "startDateTime",
        "custom_properties": "customProperties",
        "event_cancelled": "eventCancelled",
        "event_organizer": "eventOrganizer",
        "event_url": "eventUrl",
        "event_description": "eventDescription",
        "event_name": "eventName",
        "event_type": "eventType",
        "event_completed": "eventCompleted",
        "end_date_time": "endDateTime",
    }

    def __init__(
        self,
        start_date_time=None,
        custom_properties=None,
        event_cancelled=None,
        event_organizer=None,
        event_url=None,
        event_description=None,
        event_name=None,
        event_type=None,
        event_completed=None,
        end_date_time=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """MarketingEventUpdateRequestParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start_date_time = None
        self._custom_properties = None
        self._event_cancelled = None
        self._event_organizer = None
        self._event_url = None
        self._event_description = None
        self._event_name = None
        self._event_type = None
        self._event_completed = None
        self._end_date_time = None
        self.discriminator = None

        if start_date_time is not None:
            self.start_date_time = start_date_time
        if custom_properties is not None:
            self.custom_properties = custom_properties
        if event_cancelled is not None:
            self.event_cancelled = event_cancelled
        if event_organizer is not None:
            self.event_organizer = event_organizer
        if event_url is not None:
            self.event_url = event_url
        if event_description is not None:
            self.event_description = event_description
        if event_name is not None:
            self.event_name = event_name
        if event_type is not None:
            self.event_type = event_type
        if event_completed is not None:
            self.event_completed = event_completed
        if end_date_time is not None:
            self.end_date_time = end_date_time

    @property
    def start_date_time(self):
        """Gets the start_date_time of this MarketingEventUpdateRequestParams.  # noqa: E501

        The start date and time of the marketing event.  # noqa: E501

        :return: The start_date_time of this MarketingEventUpdateRequestParams.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this MarketingEventUpdateRequestParams.

        The start date and time of the marketing event.  # noqa: E501

        :param start_date_time: The start_date_time of this MarketingEventUpdateRequestParams.  # noqa: E501
        :type start_date_time: datetime
        """

        self._start_date_time = start_date_time

    @property
    def custom_properties(self):
        """Gets the custom_properties of this MarketingEventUpdateRequestParams.  # noqa: E501

        A list of PropertyValues. These can be whatever kind of property names and values you want. However, they must already exist on the HubSpot account's definition of the MarketingEvent Object. If they don't they will be filtered out and not set. In order to do this you'll need to create a new PropertyGroup on the HubSpot account's MarketingEvent object for your specific app and create the Custom Property you want to track on that HubSpot account. Do not create any new default properties on the MarketingEvent object as that will apply to all HubSpot accounts.   # noqa: E501

        :return: The custom_properties of this MarketingEventUpdateRequestParams.  # noqa: E501
        :rtype: list[PropertyValue]
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this MarketingEventUpdateRequestParams.

        A list of PropertyValues. These can be whatever kind of property names and values you want. However, they must already exist on the HubSpot account's definition of the MarketingEvent Object. If they don't they will be filtered out and not set. In order to do this you'll need to create a new PropertyGroup on the HubSpot account's MarketingEvent object for your specific app and create the Custom Property you want to track on that HubSpot account. Do not create any new default properties on the MarketingEvent object as that will apply to all HubSpot accounts.   # noqa: E501

        :param custom_properties: The custom_properties of this MarketingEventUpdateRequestParams.  # noqa: E501
        :type custom_properties: list[PropertyValue]
        """

        self._custom_properties = custom_properties

    @property
    def event_cancelled(self):
        """Gets the event_cancelled of this MarketingEventUpdateRequestParams.  # noqa: E501

        Indicates if the marketing event has been cancelled. Defaults to `false`  # noqa: E501

        :return: The event_cancelled of this MarketingEventUpdateRequestParams.  # noqa: E501
        :rtype: bool
        """
        return self._event_cancelled

    @event_cancelled.setter
    def event_cancelled(self, event_cancelled):
        """Sets the event_cancelled of this MarketingEventUpdateRequestParams.

        Indicates if the marketing event has been cancelled. Defaults to `false`  # noqa: E501

        :param event_cancelled: The event_cancelled of this MarketingEventUpdateRequestParams.  # noqa: E501
        :type event_cancelled: bool
        """

        self._event_cancelled = event_cancelled

    @property
    def event_organizer(self):
        """Gets the event_organizer of this MarketingEventUpdateRequestParams.  # noqa: E501

        The name of the organizer of the marketing event.  # noqa: E501

        :return: The event_organizer of this MarketingEventUpdateRequestParams.  # noqa: E501
        :rtype: str
        """
        return self._event_organizer

    @event_organizer.setter
    def event_organizer(self, event_organizer):
        """Sets the event_organizer of this MarketingEventUpdateRequestParams.

        The name of the organizer of the marketing event.  # noqa: E501

        :param event_organizer: The event_organizer of this MarketingEventUpdateRequestParams.  # noqa: E501
        :type event_organizer: str
        """

        self._event_organizer = event_organizer

    @property
    def event_url(self):
        """Gets the event_url of this MarketingEventUpdateRequestParams.  # noqa: E501

        A URL in the external event application where the marketing event can be managed.  # noqa: E501

        :return: The event_url of this MarketingEventUpdateRequestParams.  # noqa: E501
        :rtype: str
        """
        return self._event_url

    @event_url.setter
    def event_url(self, event_url):
        """Sets the event_url of this MarketingEventUpdateRequestParams.

        A URL in the external event application where the marketing event can be managed.  # noqa: E501

        :param event_url: The event_url of this MarketingEventUpdateRequestParams.  # noqa: E501
        :type event_url: str
        """

        self._event_url = event_url

    @property
    def event_description(self):
        """Gets the event_description of this MarketingEventUpdateRequestParams.  # noqa: E501

        The description of the marketing event.  # noqa: E501

        :return: The event_description of this MarketingEventUpdateRequestParams.  # noqa: E501
        :rtype: str
        """
        return self._event_description

    @event_description.setter
    def event_description(self, event_description):
        """Sets the event_description of this MarketingEventUpdateRequestParams.

        The description of the marketing event.  # noqa: E501

        :param event_description: The event_description of this MarketingEventUpdateRequestParams.  # noqa: E501
        :type event_description: str
        """

        self._event_description = event_description

    @property
    def event_name(self):
        """Gets the event_name of this MarketingEventUpdateRequestParams.  # noqa: E501

        The name of the marketing event.  # noqa: E501

        :return: The event_name of this MarketingEventUpdateRequestParams.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this MarketingEventUpdateRequestParams.

        The name of the marketing event.  # noqa: E501

        :param event_name: The event_name of this MarketingEventUpdateRequestParams.  # noqa: E501
        :type event_name: str
        """

        self._event_name = event_name

    @property
    def event_type(self):
        """Gets the event_type of this MarketingEventUpdateRequestParams.  # noqa: E501

        Describes what type of event this is.  For example: `WEBINAR`, `CONFERENCE`, `WORKSHOP`  # noqa: E501

        :return: The event_type of this MarketingEventUpdateRequestParams.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this MarketingEventUpdateRequestParams.

        Describes what type of event this is.  For example: `WEBINAR`, `CONFERENCE`, `WORKSHOP`  # noqa: E501

        :param event_type: The event_type of this MarketingEventUpdateRequestParams.  # noqa: E501
        :type event_type: str
        """

        self._event_type = event_type

    @property
    def event_completed(self):
        """Gets the event_completed of this MarketingEventUpdateRequestParams.  # noqa: E501


        :return: The event_completed of this MarketingEventUpdateRequestParams.  # noqa: E501
        :rtype: bool
        """
        return self._event_completed

    @event_completed.setter
    def event_completed(self, event_completed):
        """Sets the event_completed of this MarketingEventUpdateRequestParams.


        :param event_completed: The event_completed of this MarketingEventUpdateRequestParams.  # noqa: E501
        :type event_completed: bool
        """

        self._event_completed = event_completed

    @property
    def end_date_time(self):
        """Gets the end_date_time of this MarketingEventUpdateRequestParams.  # noqa: E501

        The end date and time of the marketing event.  # noqa: E501

        :return: The end_date_time of this MarketingEventUpdateRequestParams.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this MarketingEventUpdateRequestParams.

        The end date and time of the marketing event.  # noqa: E501

        :param end_date_time: The end_date_time of this MarketingEventUpdateRequestParams.  # noqa: E501
        :type end_date_time: datetime
        """

        self._end_date_time = end_date_time

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
        if not isinstance(other, MarketingEventUpdateRequestParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarketingEventUpdateRequestParams):
            return True

        return self.to_dict() != other.to_dict()
