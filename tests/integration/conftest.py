import hubspot
import pytest
import os


@pytest.fixture
def api_client():
    client = hubspot.Client.create(access_token=os.getenv("HUBSPOT_ACCESS_TOKEN"))

    return client
