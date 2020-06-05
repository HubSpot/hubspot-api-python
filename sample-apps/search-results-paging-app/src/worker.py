import os
from services.logger import logger
from helpers.search import search_next_contacts_batch


def iterate_via_search_results(search_query, process_contact_func):
    after = 0
    while True:
        contacts = search_next_contacts_batch(
            search_query=search_query, after=after, limit=os.getenv("SEARCH_BATCH_SIZE")
        )
        if len(contacts) == 0:
            break

        for contact in contacts:
            process_contact_func(contact)

        after = contacts[-1].id


if __name__ == "__main__":
    iterate_via_search_results(
        search_query=os.getenv("SEARCH_QUERY"),
        process_contact_func=lambda contact: logger.info(
            "Processing contact_id={}".format(contact.id)
        ),
    )
