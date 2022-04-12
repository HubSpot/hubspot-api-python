from hubspot import HubSpot
from hubspot.settings.users import RolesApi, TeamsApi, UsersApi


def test_is_discoverable():
    apis = HubSpot().settings.users
    assert isinstance(apis.roles_api, RolesApi)
    assert isinstance(apis.teams_api, TeamsApi)
    assert isinstance(apis.users_api, UsersApi)
