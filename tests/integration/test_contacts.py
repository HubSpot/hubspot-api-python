import time

import pytest

from hubspot.crm.contacts import PublicObjectSearchRequest
from hubspot.crm.contacts.exceptions import NotFoundException

CONTACT_PROPERTIES = {
    "properties": {
        "email": "rRocket@TestCompany.net",
        "lastname": "Rocket",
        "firstname": "Racoon"
    }
}


@pytest.fixture
def get_or_create_contact(api_client):
    try:
        contact = api_client.crm.contacts.basic_api.get_by_id(
            contact_id=CONTACT_PROPERTIES["properties"]["email"],
            id_property="email"
        )
    except NotFoundException:
        contact = api_client.crm.contacts.basic_api.create(CONTACT_PROPERTIES)
    time.sleep(3)

    yield contact

    api_client.crm.contacts.basic_api.archive(contact_id=contact.id)


@pytest.fixture
def get_or_create_company(api_client):
    properties = {
        "properties": {
            "domain": "TestCompany.net",
            "name": "TestCompany"
        }
    }
    try:
        company = api_client.crm.contacts.basic_api.get_by_id(
            contact_id=properties["properties"]["domain"],
            id_property="domain"
        )
    except NotFoundException:
        company = api_client.crm.companies.basic_api.create(properties)
    time.sleep(2)

    yield company

    api_client.crm.companies.basic_api.archive(company_id=company.id)


def get_or_create_contact_associated_with_company(api_client, get_or_create_company):
    contact_data = {
        "associations": [
            {
                "to": {"id": get_or_create_company.id},
                "types": [
                    {
                        "associationCategory": "HUBSPOT_DEFINED",
                        "associationTypeId": 1
                    }
                ]
            }
        ],
        "properties": CONTACT_PROPERTIES["properties"]
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


def test_create_contact_with_company_association(api_client, get_or_create_company):
    contact = get_or_create_contact_associated_with_company(api_client, get_or_create_company)

    assert contact


def test_contact__get_or_create(api_client, get_or_create_contact):
    assert get_or_create_contact


def test_contact__get_page(api_client):
    result = api_client.crm.contacts.basic_api.get_page()

    assert result


def test_contact__get_by_id(api_client, get_or_create_contact):
    result = api_client.crm.contacts.basic_api.get_by_id(
        contact_id=get_or_create_contact.id
    )

    assert result


def test_contact__get_all(api_client):
    result = api_client.crm.contacts.get_all()

    assert result


def test_contact__update(api_client, get_or_create_contact):
    simple_public_object_input = {
        "properties": {
            "firstname": "updated_name"
        }
    }

    result = api_client.crm.contacts.basic_api.update(get_or_create_contact.id, simple_public_object_input)

    assert result.properties["firstname"] == simple_public_object_input["properties"]["firstname"]


def test_contact__archive(api_client, get_or_create_contact):
    result = api_client.crm.contacts.basic_api.archive(get_or_create_contact.id)

    assert result is None


def test_contact__do_search(api_client, get_or_create_contact):
    public_object_search_request = PublicObjectSearchRequest(
        filter_groups=[
            {
                "filters": [
                    {
                        "value": CONTACT_PROPERTIES["properties"]["email"],
                        "propertyName": "email",
                        "operator": "EQ"
                    }
                ]
            }
        ]
    )
    time.sleep(2)
    contact = api_client.crm.contacts.search_api.do_search(public_object_search_request)

    assert contact.results
