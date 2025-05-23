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


class MarketingEventPublicReadResponseV2(object):
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
        "registrants": "int",
        "event_organizer": "str",
        "event_url": "str",
        "attendees": "int",
        "app_info": "AppInfo",
        "event_type": "str",
        "event_completed": "bool",
        "end_date_time": "datetime",
        "no_shows": "int",
        "cancellations": "int",
        "created_at": "datetime",
        "start_date_time": "datetime",
        "custom_properties": "list[CrmPropertyWrapper]",
        "event_cancelled": "bool",
        "external_event_id": "str",
        "event_status": "str",
        "event_description": "str",
        "event_name": "str",
        "object_id": "str",
        "updated_at": "datetime",
    }

    attribute_map = {
        "registrants": "registrants",
        "event_organizer": "eventOrganizer",
        "event_url": "eventUrl",
        "attendees": "attendees",
        "app_info": "appInfo",
        "event_type": "eventType",
        "event_completed": "eventCompleted",
        "end_date_time": "endDateTime",
        "no_shows": "noShows",
        "cancellations": "cancellations",
        "created_at": "createdAt",
        "start_date_time": "startDateTime",
        "custom_properties": "customProperties",
        "event_cancelled": "eventCancelled",
        "external_event_id": "externalEventId",
        "event_status": "eventStatus",
        "event_description": "eventDescription",
        "event_name": "eventName",
        "object_id": "objectId",
        "updated_at": "updatedAt",
    }

    def __init__(
        self,
        registrants=None,
        event_organizer=None,
        event_url=None,
        attendees=None,
        app_info=None,
        event_type=None,
        event_completed=None,
        end_date_time=None,
        no_shows=None,
        cancellations=None,
        created_at=None,
        start_date_time=None,
        custom_properties=None,
        event_cancelled=None,
        external_event_id=None,
        event_status=None,
        event_description=None,
        event_name=None,
        object_id=None,
        updated_at=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """MarketingEventPublicReadResponseV2 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._registrants = None
        self._event_organizer = None
        self._event_url = None
        self._attendees = None
        self._app_info = None
        self._event_type = None
        self._event_completed = None
        self._end_date_time = None
        self._no_shows = None
        self._cancellations = None
        self._created_at = None
        self._start_date_time = None
        self._custom_properties = None
        self._event_cancelled = None
        self._external_event_id = None
        self._event_status = None
        self._event_description = None
        self._event_name = None
        self._object_id = None
        self._updated_at = None
        self.discriminator = None

        if registrants is not None:
            self.registrants = registrants
        if event_organizer is not None:
            self.event_organizer = event_organizer
        if event_url is not None:
            self.event_url = event_url
        if attendees is not None:
            self.attendees = attendees
        if app_info is not None:
            self.app_info = app_info
        if event_type is not None:
            self.event_type = event_type
        if event_completed is not None:
            self.event_completed = event_completed
        if end_date_time is not None:
            self.end_date_time = end_date_time
        if no_shows is not None:
            self.no_shows = no_shows
        if cancellations is not None:
            self.cancellations = cancellations
        self.created_at = created_at
        if start_date_time is not None:
            self.start_date_time = start_date_time
        self.custom_properties = custom_properties
        if event_cancelled is not None:
            self.event_cancelled = event_cancelled
        if external_event_id is not None:
            self.external_event_id = external_event_id
        if event_status is not None:
            self.event_status = event_status
        if event_description is not None:
            self.event_description = event_description
        self.event_name = event_name
        self.object_id = object_id
        self.updated_at = updated_at

    @property
    def registrants(self):
        """Gets the registrants of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The registrants of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: int
        """
        return self._registrants

    @registrants.setter
    def registrants(self, registrants):
        """Sets the registrants of this MarketingEventPublicReadResponseV2.


        :param registrants: The registrants of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type registrants: int
        """

        self._registrants = registrants

    @property
    def event_organizer(self):
        """Gets the event_organizer of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The event_organizer of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._event_organizer

    @event_organizer.setter
    def event_organizer(self, event_organizer):
        """Sets the event_organizer of this MarketingEventPublicReadResponseV2.


        :param event_organizer: The event_organizer of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type event_organizer: str
        """

        self._event_organizer = event_organizer

    @property
    def event_url(self):
        """Gets the event_url of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The event_url of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._event_url

    @event_url.setter
    def event_url(self, event_url):
        """Sets the event_url of this MarketingEventPublicReadResponseV2.


        :param event_url: The event_url of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type event_url: str
        """

        self._event_url = event_url

    @property
    def attendees(self):
        """Gets the attendees of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The attendees of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: int
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees):
        """Sets the attendees of this MarketingEventPublicReadResponseV2.


        :param attendees: The attendees of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type attendees: int
        """

        self._attendees = attendees

    @property
    def app_info(self):
        """Gets the app_info of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The app_info of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: AppInfo
        """
        return self._app_info

    @app_info.setter
    def app_info(self, app_info):
        """Sets the app_info of this MarketingEventPublicReadResponseV2.


        :param app_info: The app_info of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type app_info: AppInfo
        """

        self._app_info = app_info

    @property
    def event_type(self):
        """Gets the event_type of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The event_type of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this MarketingEventPublicReadResponseV2.


        :param event_type: The event_type of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type event_type: str
        """

        self._event_type = event_type

    @property
    def event_completed(self):
        """Gets the event_completed of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The event_completed of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: bool
        """
        return self._event_completed

    @event_completed.setter
    def event_completed(self, event_completed):
        """Sets the event_completed of this MarketingEventPublicReadResponseV2.


        :param event_completed: The event_completed of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type event_completed: bool
        """

        self._event_completed = event_completed

    @property
    def end_date_time(self):
        """Gets the end_date_time of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The end_date_time of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this MarketingEventPublicReadResponseV2.


        :param end_date_time: The end_date_time of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type end_date_time: datetime
        """

        self._end_date_time = end_date_time

    @property
    def no_shows(self):
        """Gets the no_shows of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The no_shows of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: int
        """
        return self._no_shows

    @no_shows.setter
    def no_shows(self, no_shows):
        """Sets the no_shows of this MarketingEventPublicReadResponseV2.


        :param no_shows: The no_shows of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type no_shows: int
        """

        self._no_shows = no_shows

    @property
    def cancellations(self):
        """Gets the cancellations of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The cancellations of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: int
        """
        return self._cancellations

    @cancellations.setter
    def cancellations(self, cancellations):
        """Sets the cancellations of this MarketingEventPublicReadResponseV2.


        :param cancellations: The cancellations of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type cancellations: int
        """

        self._cancellations = cancellations

    @property
    def created_at(self):
        """Gets the created_at of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The created_at of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MarketingEventPublicReadResponseV2.


        :param created_at: The created_at of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def start_date_time(self):
        """Gets the start_date_time of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The start_date_time of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this MarketingEventPublicReadResponseV2.


        :param start_date_time: The start_date_time of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type start_date_time: datetime
        """

        self._start_date_time = start_date_time

    @property
    def custom_properties(self):
        """Gets the custom_properties of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The custom_properties of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: list[CrmPropertyWrapper]
        """
        return self._custom_properties

    @custom_properties.setter
    def custom_properties(self, custom_properties):
        """Sets the custom_properties of this MarketingEventPublicReadResponseV2.


        :param custom_properties: The custom_properties of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type custom_properties: list[CrmPropertyWrapper]
        """
        if self.local_vars_configuration.client_side_validation and custom_properties is None:  # noqa: E501
            raise ValueError("Invalid value for `custom_properties`, must not be `None`")  # noqa: E501

        self._custom_properties = custom_properties

    @property
    def event_cancelled(self):
        """Gets the event_cancelled of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The event_cancelled of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: bool
        """
        return self._event_cancelled

    @event_cancelled.setter
    def event_cancelled(self, event_cancelled):
        """Sets the event_cancelled of this MarketingEventPublicReadResponseV2.


        :param event_cancelled: The event_cancelled of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type event_cancelled: bool
        """

        self._event_cancelled = event_cancelled

    @property
    def external_event_id(self):
        """Gets the external_event_id of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The external_event_id of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._external_event_id

    @external_event_id.setter
    def external_event_id(self, external_event_id):
        """Sets the external_event_id of this MarketingEventPublicReadResponseV2.


        :param external_event_id: The external_event_id of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type external_event_id: str
        """

        self._external_event_id = external_event_id

    @property
    def event_status(self):
        """Gets the event_status of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The event_status of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        """Sets the event_status of this MarketingEventPublicReadResponseV2.


        :param event_status: The event_status of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type event_status: str
        """

        self._event_status = event_status

    @property
    def event_description(self):
        """Gets the event_description of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The event_description of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._event_description

    @event_description.setter
    def event_description(self, event_description):
        """Sets the event_description of this MarketingEventPublicReadResponseV2.


        :param event_description: The event_description of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type event_description: str
        """

        self._event_description = event_description

    @property
    def event_name(self):
        """Gets the event_name of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The event_name of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this MarketingEventPublicReadResponseV2.


        :param event_name: The event_name of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type event_name: str
        """
        if self.local_vars_configuration.client_side_validation and event_name is None:  # noqa: E501
            raise ValueError("Invalid value for `event_name`, must not be `None`")  # noqa: E501

        self._event_name = event_name

    @property
    def object_id(self):
        """Gets the object_id of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The object_id of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this MarketingEventPublicReadResponseV2.


        :param object_id: The object_id of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :type object_id: str
        """
        if self.local_vars_configuration.client_side_validation and object_id is None:  # noqa: E501
            raise ValueError("Invalid value for `object_id`, must not be `None`")  # noqa: E501

        self._object_id = object_id

    @property
    def updated_at(self):
        """Gets the updated_at of this MarketingEventPublicReadResponseV2.  # noqa: E501


        :return: The updated_at of this MarketingEventPublicReadResponseV2.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this MarketingEventPublicReadResponseV2.


        :param updated_at: The updated_at of this MarketingEventPublicReadResponseV2.  # noqa: E501
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
        if not isinstance(other, MarketingEventPublicReadResponseV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarketingEventPublicReadResponseV2):
            return True

        return self.to_dict() != other.to_dict()
