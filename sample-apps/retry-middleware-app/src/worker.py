from helpers.hubspot import create_client
from helpers.oauth import is_authorized
from services.logger import logger
from hubspot.crm.contacts import ApiException
from multiprocessing import Process
import os
import time
import sys


def call_api():
    # Pay attention on create_client.
    # It generates a client with reties middlewares.
    hubspot = create_client()
    try:
        page = hubspot.crm.contacts.basic_api.get_page()
        if os.getppid() == 0:
            logger.info("Requesting get_page: success")
    except ApiException as e:
        logger.error("Exception occurred, status code: ".format(e.status))


def circle():
    for i in range(100):
        try:
            call_api()
        except KeyboardInterrupt:
            sys.exit(0)


if not is_authorized():
    print(
        "In order to continue please go to http://localhost:5000 and authorize via OAuth."
    )
    print("Then return back")

    while True:
        if not is_authorized():
            time.sleep(3)
        else:
            break


for i in range(int(os.environ.get("PROCESS_COUNT"))):
    process = Process(target=circle).start()

circle()
