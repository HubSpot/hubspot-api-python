# hubspot-api-python

Python [HubSpot API](https://developers.hubspot.com/docs/api/overview) v3 SDK(Client) files and sample apps

Sample Applications can be found in [Sample apps](https://github.com/HubSpot/sample-apps-list)

## Documentation

See the [API docs](https://developers.hubspot.com/docs/api/overview).

## Installation

If you just want to use the package, run:

```bash
pip install --upgrade hubspot-api-client
```

### Requirements

Make sure you have [Python 3.7+](https://docs.python.org/3/) and [pip](https://pypi.org/project/pip/) installed.


## Quickstart


### Configuring HubSpot client

```python
from hubspot import HubSpot

api_client = HubSpot(access_token='your_access_token')

# or set your access token later
api_client = HubSpot()
api_client.access_token = 'your_access_token'
```

You'll need to create a [private app](https://developers.hubspot.com/docs/api/private-apps) to get your access token or you can obtain OAuth2 access token.

#### Hapikey support:

Please, note that hapikey is no longer supported after v5.1.0. You can get more info about hapikey sunset [here](https://developers.hubspot.com/changelog/upcoming-api-key-sunset). Also, plese, visit a [migration guide](https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app) if you need help with a migration process.

### OAuth API

#### Obtain OAuth2 access token:

```python
from hubspot.oauth import ApiException

try:
    tokens = api_client.oauth.tokens_api.create(
        grant_type="authorization_code",
        redirect_uri='http://localhost',
        client_id='client_id',
        client_secret='client_secret',
        code='code'
    )
except ApiException as e:
    print("Exception when calling create_token method: %s\n" % e)
```

### CRM API


#### Create contact:

```python
from hubspot.crm.contacts import SimplePublicObjectInputForCreate
from hubspot.crm.contacts.exceptions import ApiException

try:
    simple_public_object_input_for_create = SimplePublicObjectInputForCreate(
        properties={"email": "email@example.com"}
    )
    api_response = api_client.crm.contacts.basic_api.create(
        simple_public_object_input_for_create=simple_public_object_input_for_create
    )
except ApiException as e:
    print("Exception when creating contact: %s\n" % e)
```

#### Get contact by id:

```python
from hubspot.crm.contacts import ApiException

try:
    contact_fetched = api_client.crm.contacts.basic_api.get_by_id('contact_id')
except ApiException as e:
    print("Exception when requesting contact by id: %s\n" % e)
```

#### Get custom objects page:

```python
from hubspot.crm.objects import ApiException

try:
    my_custom_objects_page = api_client.crm.objects.basic_api.get_page(object_type="my_custom_object_type")
except ApiException as e:
    print("Exception when requesting custom objects: %s\n" % e)
```

#### Get all:

`get_all` method is available for all objects (Companies, Contacts, Deals and etc).

```python
all_contacts = api_client.crm.contacts.get_all()
```

Please note that pagination is used under the hood to get all results.

## Search:

`do_search` method is available for all objects (Companies, Contacts, Deals and etc).

### Example Search by date:
```python
import hubspot

from dateutil import parser
from pprint import pprint
from hubspot.crm.contacts import PublicObjectSearchRequest, ApiException

api_client = hubspot.Client.create(access_token="YOUR_ACCESS_TOKEN")

# timestamp in milliseconds
date = str(int(parser.isoparse("XXXX-XX-XXTXX:XX:XX.XXXZ").timestamp() * 1000))
public_object_search_request = PublicObjectSearchRequest(
    filter_groups=[
        {
            "filters": [
                {
                    "value": date,
                    "propertyName": "lastmodifieddate",
                    "operator": "EQ"
                }
            ]
        }
    ], limit=10
)
try:
    api_response = api_client.crm.contacts.search_api.do_search(public_object_search_request=public_object_search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling search_api->do_search: %s\n" % e)

```

### CMS API

#### Get audit logs:

```python
from hubspot.cms.audit_logs import ApiException

try:
    audit_logs_page = api_client.cms.audit_logs.default_api.get_page()
except ApiException as e:
    print("Exception when calling cards_api->create: %s\n" % e)
```

### Files API

#### Upload files:
```python
import hubspot
import json
from pprint import pprint
from hubspot.crm.contacts import ApiException

client = hubspot.Client.create(access_token="your_access_token")

options = json.dumps(
    {'access': 'PRIVATE',
     "overwrite": False}
)

try:
    response = client.files.files_api.upload(
        file="/file/path/file.jpeg",
        file_name="name_in_hubspot",
        folder_path="folder_in_hubspot",
        options=options,
    )
    pprint(response)

except ApiException as e:
    print("Exception when calling basic_api->get_page: %s\n" % e)
```

## Not wrapped endpoint(s)

It is possible to access the hubspot request method directly,
it could be handy if client doesn't have implementation for some endpoint yet.
Exposed request method benefits by having all configured client params.

```python
client.api_request({
    "method": "PUT",
    "path": "/some/api/not/wrapped/yet",
    "body": {"key": "value"}
})
```

### {Example} for `GET` request

```python
import hubspot
from pprint import pprint
from hubspot.crm.contacts import ApiException

client = hubspot.Client.create(access_token="your_access_token")

try:
    response = client.api_request(
        {"path": "/crm/v3/objects/contacts"}
    )
    pprint(response)
except ApiException as e:
    print(e)
```

### {Example} for `POST` request

```python
import hubspot
from pprint import pprint
from hubspot.crm.contacts import ApiException

client = hubspot.Client.create(access_token="your_access_token")

try:
    response = client.api_request(
        {
            "path": "/crm/v3/objects/contacts",
            "method": "POST",
            "body": {
                "properties":
                    {
                        "email": "some_email@some.com",
                        "lastname": "some_last_name"
                    },
            }
        }

    )
    pprint(response.json())
except ApiException as e:
    print(e)
```
### Using utils

#### Get OAuth url:

```python
from hubspot.utils.oauth import get_auth_url

auth_url = get_auth_url(
    scope=('contacts',),
    client_id='client_id',
    redirect_uri='http://localhost'
)
```

#### Validate HubSpot request signature

[Example](./sample-apps/webhooks-app/src/routes/webhooks.py) of usage from [Webhooks Sample App](./sample-apps/webhooks-app):

```python
import os
from flask import request
from hubspot.utils.signature import Signature

Signature.is_valid(
    signature=request.headers["X-HubSpot-Signature"],
    client_secret=os.getenv("HUBSPOT_CLIENT_SECRET"),
    request_body=request.data.decode("utf-8"),
    http_uri=request.base_url,
    signature_version=request.headers["X-HubSpot-Signature-Version"],
    timestamp=request.headers["X-HubSpot-Request-Timestamp"]
)
```

### Retry middleware

You can pass an instance of [urllib3.util.retry.Retry](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html) class to configure http client retries.
With internal error retry middleware:

```python
from hubspot import HubSpot
from urllib3.util.retry import Retry

retry = Retry(
    total=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
)
api_client = HubSpot(retry=retry)
```
Or with rate limit retry middleware:

```python
from hubspot import HubSpot
from urllib3.util.retry import Retry

retry = Retry(
    total=5,
    status_forcelist=(429,),
)
api_client = HubSpot(retry=retry)
```

### Convert response object to dict

`to_dict` method is available for most response objects

```python
contacts = api_client.crm.contacts.basic_api.get_page()
for contact in contacts.results:
    print(contact.to_dict())
```

## Sample Apps

Please, take a look at our [Sample apps](https://github.com/HubSpot/sample-apps-list)

## Contributing

Install the package locally:

```
pip install -e .
```

Set up the development virtualenv:

```
make
```

Run tests:
```
make test
```

Run [Black](https://github.com/psf/black) for code formatting:
```
make fmt
```
