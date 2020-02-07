# hubspot-api-python

Python [HubSpot API](https://developers.hubspot.com/docs-beta/overview) v3 SDK(Client) files and sample apps

Sample Applications can be found in [sample-apps](sample-apps/) folder

## Quickstart

To obtain access OAuth2 access token run the following:

```python
import hubspot

oauth_client = hubspot.Client.create().auth().oauth()

try:
    tokens = oauth_client.default_api().create_token(
        grant_type="authorization_code",
        redirect_uri='http://localhost',
        client_id='client_id',
        client_secret='client_secret',
        code='code'
    )
except oauth_client.exceptions().ApiException as e:
    print("Exception when calling create_token method: %s\n" % e)
```