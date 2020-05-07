import time
import os
import random
from redis_ratelimit import ratelimit
from redis_ratelimit.exceptions import RateLimited
from helpers.hubspot import create_client
from services.logger import logger
from hubspot.crm.contacts import ApiException


@ratelimit(rate=os.getenv("RATE_LIMIT"), key='api_call', redis_url=os.getenv("REDIS_URL"))
def call_api():
    hubspot = create_client()
    try:
        hubspot.crm.contacts.basic_api.get_page()
        logger.info("Requesting get_page: success")
    except ApiException as e:
        logger.error("Exception occurred, status code: ".format(e.status))


while True:
    try:
        call_api()
    except RateLimited:
        logger.warning('Rate limit reached, sleeping...')
        time.sleep(0.5 + random.random())
