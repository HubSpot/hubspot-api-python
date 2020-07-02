import time
import sys
import os
import random
from redis_ratelimit import ratelimit
from redis_ratelimit.exceptions import RateLimited
from helpers.hubspot import create_client
from services.logger import logger
from hubspot.crm.contacts import ApiException
from helpers.oauth import is_authorized


@ratelimit(
    rate=os.getenv("RATE_LIMIT"), key="api_call", redis_url=os.getenv("REDIS_URL")
)
def call_api():
    hubspot = create_client()
    try:
        hubspot.crm.contacts.basic_api.get_page()
        logger.info("Requesting get_page: success")
    except ApiException as e:
        logger.error("Exception occurred, status code: ".format(e.status))


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

try:
    while True:
        try:
            call_api()
        except RateLimited:
            logger.warning("Rate limit reached, sleeping...")
            time.sleep(0.5 + random.random())
except KeyboardInterrupt:
    sys.exit(0)
