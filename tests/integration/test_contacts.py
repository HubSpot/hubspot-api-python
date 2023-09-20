import pytest

from hubspot.crm.contacts import PublicObjectSearchRequest

CONTACT_PROPERTIES = {
    "email": "bcooper@biglytics.net",
    "lastname": "Cooper",
    "firstname": "Bryan"
}


@pytest.fixture
def create_contact(api_client):
    contact = api_client.crm.contacts.basic_api.create(CONTACT_PROPERTIES)

    yield contact

    api_client.crm.contacts.basic_api.archive(contact_id=contact.id)


@pytest.fixture
def create_company(api_client):
    properties = {
        "domain": "biglytics.net",
        "name": "Biglytics",
    }

    company = api_client.crm.companies.basic_api.create(properties)

    yield company

    api_client.crm.companies.basic_api.archive(company_id=company.id)


def get_or_create_contact_associated_with_company(api_client, create_company):
    contact_data = {
        "associations": [
            {
                "to": {"id": create_company.id},
                "types": [
                    {
                        "associationCategory": "HUBSPOT_DEFINED",
                        "associationTypeId": 1
                    }
                ]
            }
        ],
        "properties": CONTACT_PROPERTIES
    }
    public_object_search_request = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {
                        "value": contact_data["properties"]["email"],
                        "propertyName": "email",
                        "operator": "EQ"
                    }
                ]
            }
        ]
    )
    contact_response = api_client.crm.contacts.search_api.do_search(public_object_search_request)
    if contact_response.results:
        return contact_response.results[0]
    else:
        return api_client.crm.contacts.basic_api.create(contact_data)


def test_create_contact_with_company_association(api_client, create_company):
    contact = get_or_create_contact_associated_with_company(api_client, create_company)

    assert contact


def test_contact__create(api_client):
    contact = api_client.crm.contacts.basic_api.create(CONTACT_PROPERTIES)

    assert contact

    api_client.crm.contacts.basic_api.archive(contact_id=contact.id)


def test_contact__get_page(api_client):
    result = api_client.crm.companies.basic_api.get_page()

    assert result


def test_contact__get_by_id(api_client, create_contact):
    result = api_client.crm.contacts.basic_api.get_by_id(create_contact.id)

    assert result


def test_contact__get_all(api_client):
    result = api_client.crm.contacts.get_all()

    assert result


def test_contact__update(api_client, create_contact):
    simple_public_object_input = {
        "properties": {
            "firstname": "updated_name"
        }
    }

    result = api_client.crm.contacts.basic_api.update(create_contact.id, simple_public_object_input)

    assert result.properties["firstname"] == simple_public_object_input["properties"]["firstname"]


def test_contact__archive(api_client, create_contact):
    result = api_client.crm.contacts.basic_api.archive(create_contact.id)

    assert result is None


def test_contact__do_search(api_client, create_contact):
    public_object_search_request = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {
                        "value": "bcooper@biglytics.net",
                        "propertyName": "email",
                        "operator": "EQ"
                    }
                ]
            }
        ]
    )
    contact = api_client.crm.contacts.search_api.do_search(public_object_search_request)

    assert contact.results
