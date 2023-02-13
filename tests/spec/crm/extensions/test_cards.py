from hubspot import HubSpot
from hubspot.crm.extensions.cards import CardsApi, SampleResponseApi


def test_is_discoverable():
    apis = HubSpot().crm.extensions.cards
    assert isinstance(apis.cards_api, CardsApi)
    assert isinstance(apis.sample_response_api, SampleResponseApi)
