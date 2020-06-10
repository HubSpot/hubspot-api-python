# hubspot-api-python

Python [HubSpot API](https://developers.hubspot.com/docs/overview) v3 SDK(Client) files and sample apps

Sample Applications can be found in [sample-apps](sample-apps/) folder

## Documentation

See the [API docs](https://developers.hubspot.com/docs/overview).

## Installation

If you just want to use the package, run:

```bash
pip install --upgrade hubspot-api-client
```

### Requirements

Make sure you have [Python 3.5+](https://docs.python.org/3/) and [pip](https://pypi.org/project/pip/) installed.


## Quickstart


### Configuring HubSpot client

```python
import hubspot

client = hubspot.Client.create()
# or with api_key
client = hubspot.Client.create(api_key='your_api_key')
# or with access_token
client = hubspot.Client.create()
client.access_token = 'your_access_token'
```

### OAuth API

#### Obtain OAuth2 access token:

```python
from hubspot.auth.oauth import ApiException

oauth_client = client.auth.oauth

try:
    tokens = oauth_client.default_api.create_token(
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

#### Get contact by id:

```python
from hubspot.crm.contacts import ApiException

try:
    contact_fetched = client.crm.contacts.basic_api.get_by_id('contact_id')
except ApiException as e:
    print("Exception when requesting contact by id: %s\n" % e)
```

#### Get all:

get_all method is available for all major objects and works like

```python
all_contacts = contacts_client = client.crm.contacts.get_all()
```

Please note that pagination is used under the hood to get all results.

### CMS API

#### Get audit logs:

```python
from hubspot.cms.audit_logs.exceptions import ApiException

try:
    audit_logs_page = client.cms.audit_logs.default_api.get_page()
except ApiException as e:
    print("Exception when calling cards_api->create: %s\n" % e)
```

### Using utils

#### Get OAuth url:

```python
from hubspot.utils.oauth import get_auth_url

auth_url = get_auth_url(
    scopes=('contacts',),
    client_id='client_id',
    redirect_uri='http://localhost'
)
```

#### Validate HubSpot request signature

[Example](./sample-apps/webhooks-app/src/routes/webhooks.py) of usage from [Webhooks Sample App](./sample-apps/webhooks-app):

```python
import os
from flask import request
from hubspot.utils.webhooks import validate_signature
from hubspot.exceptions import InvalidSignatureError

try:
    validate_signature(
        signature=request.headers["X-HubSpot-Signature"],
        signature_version=request.headers["X-HubSpot-Signature-Version"],
        http_uri=request.base_url,
        request_body=request.data.decode("utf-8"),
        client_secret=os.getenv("HUBSPOT_CLIENT_SECRET"),
    )
except InvalidSignatureError:
    print("Request signature is not valid")

```

### Retry middleware

You can pass an instance of [urllib3.util.retry.Retry](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html) class to configure http client retries.
With internal error retry middleware:

```python
import hubspot
from urllib3.util.retry import Retry

retry = Retry(
    total=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
)
client = hubspot.Client.create(retry=retry)
```
Or with rate limit retry middleware:

```python
import hubspot
from urllib3.util.retry import Retry

retry = Retry(
    total=5,
    status_forcelist=(429,),
)
client = hubspot.Client.create(retry=retry)
```

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
