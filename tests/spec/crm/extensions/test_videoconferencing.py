from hubspot import HubSpot
from hubspot.crm.extensions.videoconferencing import SettingsApi

def test_is_discoverable():
    apis = HubSpot().crm.extensions.videoconferencing
    assert isinstance(apis.settings_api, SettingsApi)
