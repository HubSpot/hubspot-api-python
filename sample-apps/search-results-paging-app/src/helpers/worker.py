from hubspot.crm.contacts import (
    PublicObjectSearchRequest, BatchInputSimplePublicObjectBatchInput, SimplePublicObjectBatchInput,
    Filter, FilterGroup
)
from helpers.hubspot import create_client

hubspot = create_client()


def get_next_contacts_batch(search_started_at, limit, search_query):
    filters = [Filter(property_name="searched_at", operator="LT", value=search_started_at)]
    filter_groups = [FilterGroup(filters=filters)]
    public_object_search_request = PublicObjectSearchRequest(
        query=search_query,
        limit=limit,
        filter_groups=filter_groups
    )
    response = hubspot.crm.contacts.search_api.do_search(
        public_object_search_request=public_object_search_request,
    )

    return response.results


def update_contacts_batch(contacts, properties):
    inputs = [SimplePublicObjectBatchInput(id=contact.id, properties=properties) for contact in
              contacts]
    batch_input_simple_public_object_batch_input = BatchInputSimplePublicObjectBatchInput(
        inputs=inputs
    )
    hubspot.crm.contacts.batch_api.update(
        batch_input_simple_public_object_batch_input=batch_input_simple_public_object_batch_input
    )
