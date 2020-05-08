import hubspot
from hubspot.crm.extensions.cards import CardsApi


def test_is_discoverable():
    apis = hubspot.Client.create().crm.extensions.cards
    assert isinstance(apis.cards_api, CardsApi)
