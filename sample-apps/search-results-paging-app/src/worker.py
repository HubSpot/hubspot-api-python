import time

from services.logger import logger
from helpers.worker import get_next_contacts_batch, update_contacts_batch


def iterate_via_search_results(search_query, process_contact_func):
    search_started_at = int(time.time())
    while True:
        contacts = get_next_contacts_batch(search_started_at=search_started_at, limit=6, search_query=search_query)
        if len(contacts) == 0:
            break

        for contact in contacts:
            process_contact_func(contact)

        update_contacts_batch(
            contacts=contacts,
            properties={"searched_at": search_started_at},
        )

        logger.info("Delay: {} seconds..".format(5))
        time.sleep(5)


if __name__ == "__main__":
    iterate_via_search_results(
        search_query="a",
        process_contact_func=lambda contact: logger.info("Processing contact_id={}".format(contact.id))
    )
