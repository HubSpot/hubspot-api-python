import pytest

from hubspot.crm import ObjectType


@pytest.mark.parametrize("test_value", ["DEALS", "TICKETS", "CONTACTS", "COMPANIES"])
def test_has_object_type(test_value):
    assert hasattr(ObjectType, test_value)
