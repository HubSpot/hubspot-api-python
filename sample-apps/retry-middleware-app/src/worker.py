from helpers.hubspot import create_client
from services.logger import logger
from hubspot.crm.contacts import ApiException


def call_api():
    #Pay attention on create_client.
    #It generates a client with reties middlewares.
    hubspot = create_client()
    try:
        hubspot.crm.contacts.basic_api.get_page()
        logger.info("Requesting get_page: success")
    except ApiException as e:
        logger.error("Exception occurred, status code: ".format(e.status))


while True:
    call_api()
