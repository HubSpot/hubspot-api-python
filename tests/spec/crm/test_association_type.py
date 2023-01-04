import pytest

from hubspot.crm import AssociationType


@pytest.mark.parametrize("test_value", ["CONTACT_TO_DEAL", "COMPANY_TO_CONTACT"])
def test_has_association_type(test_value):
    assert hasattr(AssociationType, test_value)
