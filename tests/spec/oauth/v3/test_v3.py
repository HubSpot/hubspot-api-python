import json
from unittest.mock import patch

from hubspot import HubSpot
from hubspot.oauth.v3 import AdvancedApi
from hubspot.oauth.v3.rest import RESTResponse


class FakeResponse:
    def __init__(self, body):
        self.status = 200
        self.reason = "OK"
        self.data = json.dumps(body).encode("utf-8")

    def getheaders(self):
        return {"content-type": "application/json"}

    def getheader(self, name, default=None):
        return self.getheaders().get(name.lower(), default)


def respond_with(body):
    return patch("hubspot.oauth.v3.rest.RESTClientObject.request", return_value=RESTResponse(FakeResponse(body)))


def test_is_discoverable():
    apis = HubSpot().oauth.v3
    assert isinstance(apis.advanced_api, AdvancedApi)


def test_get_token_deserializes_access_token_response():
    body = {
        "access_token": "access",
        "refresh_token": "refresh",
        "expires_in": 1800,
        "token_type": "bearer",
        "token_use": "access_token",
    }
    with respond_with(body):
        response = HubSpot().oauth.v3.advanced_api.get_token()

    assert response.access_token == "access"
    assert response.refresh_token == "refresh"
    assert response.expires_in == 1800
    assert response.token_use == "access_token"


def test_introspect_token_deserializes_refresh_token_info_response():
    body = {
        "active": True,
        "app_id": 1,
        "client_id": "client",
        "hub_id": 2,
        "scopes": ["oauth"],
        "token": "refresh",
        "token_type": "bearer",
        "token_use": "refresh_token",
        "user_id": 3,
    }
    with respond_with(body):
        response = HubSpot().oauth.v3.advanced_api.introspect_token()

    assert response.active is True
    assert response.app_id == 1
    assert response.token_use == "refresh_token"
    assert response.user_id == 3
