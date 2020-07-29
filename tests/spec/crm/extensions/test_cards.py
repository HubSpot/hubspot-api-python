from hubspot import HubSpot
from hubspot.crm.extensions.cards import CardsApi


def test_is_discoverable():
    apis = HubSpot().crm.extensions.cards
    assert isinstance(apis.cards_api, CardsApi)
