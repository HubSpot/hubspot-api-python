from hubspot import HubSpot
from hubspot.crm.extensions.calling import SettingsApi, RecordingSettingsApi


def test_is_discoverable():
    apis = HubSpot().crm.extensions.calling
    assert isinstance(apis.settings_api, SettingsApi)
    assert isinstance(apis.recording_settings_api, RecordingSettingsApi)
