import hubspot.crm.extensions.calling as api_client
from ....discovery_base import DiscoveryBase


class Discovery(DiscoveryBase):

    @property
    def channel_connection_settings_api(self) -> api_client.ChannelConnectionSettingsApi:
        return self._configure_api_client(api_client, "ChannelConnectionSettingsApi")

    @property
    def recording_settings_api(self) -> api_client.RecordingSettingsApi:
        return self._configure_api_client(api_client, "RecordingSettingsApi")

    @property
    def settings_api(self) -> api_client.SettingsApi:
        return self._configure_api_client(api_client, "SettingsApi")
