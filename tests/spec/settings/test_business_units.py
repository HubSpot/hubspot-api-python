from hubspot import HubSpot
from hubspot.settings.business_units import BusinessUnitApi


def test_is_discoverable():
    apis = HubSpot().settings.business_units
    assert isinstance(apis.business_unit_api, BusinessUnitApi)
