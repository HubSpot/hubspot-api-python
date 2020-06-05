from hubspot.crm.contacts import PublicObjectSearchRequest, Filter, FilterGroup
from helpers.hubspot import create_client

hubspot = create_client()


def search_next_contacts_batch(after, limit, search_query):
    filter_ = Filter(property_name="hs_object_id", operator="GT", value=after)
    filter_groups = [FilterGroup(filters=[filter_])]
    public_object_search_request = PublicObjectSearchRequest(
        query=search_query,
        limit=limit,
        filter_groups=filter_groups,
        sorts=[{"propertyName": "hs_object_id", "direction": "ASCENDING"}],
    )
    response = hubspot.crm.contacts.search_api.do_search(
        public_object_search_request=public_object_search_request,
    )

    return response.results
