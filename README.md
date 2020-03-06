# hubspot-api-python

Python [HubSpot API](https://developers.hubspot.com/docs-beta/overview) v3 SDK(Client) files and sample apps

Sample Applications can be found in [sample-apps](sample-apps/) folder

## Quickstart

### Dependencies

Make sure you have [Python3](https://docs.python.org/3/) and [pip](https://pypi.org/project/pip/) installed.

### Installing package locally:

Clone repository and run:

```bash
pip install -e .
```

### Configuring HubSpot client

```python
import hubspot

hubspot_client = hubspot.Client.create()
# or with api_key
hubspot_client = huspot.Client.create(api_key='my_api_key')
# or with access_token
hubspot_client = huspot.Client.create(access_token='my_access_token')
```

You can pass instance of [urllib3.util.retry.Retry](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html) to configure http client retries:

```python
import hubspot
from urllib3.util.retry import Retry

retries = Retry(
    total=3
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
)
hubspot_client = huspot.Client.create(retries=retries)
```

### Requesting API endpoints

#### Obtain OAuth2 access token:

```python
from hubspot.auth.oauth import ApiException

oauth_client = hubspot_client.auth().oauth()

try:
    tokens = oauth_client.default_api().create_token(
        grant_type="authorization_code",
        redirect_uri='http://localhost',
        client_id='client_id',
        client_secret='client_secret',
        code='code'
    )
except ApiException as e:
    print("Exception when calling create_token method: %s\n" % e)
```

#### Get contact by id:

```python
from hubspot.crm.contacts import ApiException

contacts_client = hubspot_client.crm().contacts()

try:
    contact_fetched = contacts_client.basic_api().get_by_id('contact_id')
except ApiException as e:
    print("Exception when requesting contact by id: %s\n" % e)
```

### Using utils

```python
print(hubspot.utils.oauth.get_auth_url(scopes=('contacts',), client_id='client_id', redirect_uri='http://localhost'))
```
