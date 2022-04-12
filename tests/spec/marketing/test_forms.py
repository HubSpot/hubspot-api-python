from hubspot import HubSpot
from hubspot.marketing.forms import FormsApi


def test_is_discoverable():
    apis = HubSpot().marketing.forms 
    assert isinstance(apis.forms_api, FormsApi)
