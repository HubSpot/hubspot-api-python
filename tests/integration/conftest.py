import hubspot
import pytest
import os


@pytest.fixture
def api_client():
    client = hubspot.Client.create(access_token=os.getenv("HUBSPOT_ACCESS_TOKEN"))

    return client


@pytest.fixture
def api_client_by_api_key():
    client = hubspot.Client.create(api_key=os.getenv("HUBSPOT_DEVELOPER_API_KEY"))

    return client
