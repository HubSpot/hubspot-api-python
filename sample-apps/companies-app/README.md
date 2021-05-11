# HubSpot-python sample Companies app

This is a sample app for the [hubspot-python SDK](../../../../).
Currently, this app focuses on demonstrating the functionality of [Companies API](https://developers.hubspot.com/docs/api/crm/companies) endpoints and their related actions.

Please see the documentation on [Creating an app in HubSpot](https://developers.hubspot.com/docs/api/creating-an-app)

### HubSpot Public API links used in this application

  - [Create a company object](https://developers.hubspot.com/docs/api/crm/companies)
  - [Update a company](https://developers.hubspot.com/docs/api/crm/companies)
  - [Search for companies by domain](https://developers.hubspot.com/docs/api/crm/companies)
  - [Get companies](https://developers.hubspot.com/docs/api/crm/companies)
  - [Get all company properties](https://developers.hubspot.com/docs/api/crm/properties)
  - [Get a company](https://developers.hubspot.com/docs/api/crm/companies)
  - [Get associated contacts at a company](https://developers.hubspot.com/docs/api/crm/contacts)
  - [Read a batch of contact objects by ID](https://developers.hubspot.com/docs/api/crm/companies)
  - [Get all contacts](https://developers.hubspot.com/docs/api/crm/contacts)
  - [Search for contacts](https://developers.hubspot.com/docs/api/crm/contacts)
  - [Create associations between company and contacts](https://developers.hubspot.com/docs/api/crm/associations)
  - [Delete associations between company and contacts](https://developers.hubspot.com/docs/api/crm/associations)

### Note on Application Scopes
HubSpot provides a way to restrict application users access to the system to certain scopes. In order to do that it is a good practice to make a set of scopes required by your applicatuion.
Please refer to [Initiate an Integration with OAuth 2.0](https://developers.hubspot.com/docs/methods/oauth2/initiate-oauth-integration) for documentation on the scope parameter passed to https://app.hubspot.com/oauth/authorize to make a set of scopes required. [Scopes](https://developers.hubspot.com/docs/methods/oauth2/initiate-oauth-integration#scopes) explains how to make optional scopes and talks about scopes available in HubSpot system

### Setup App

Make sure you have [Docker Compose](https://docs.docker.com/compose/) installed.

### Configure

1. Copy .env.template to .env
2. Paste your HUBSPOT_CLIENT_ID and HUBSPOT_CLIENT_SECRET

### Running

The best way to run this project (with the least configuration), is using docker compose.  Change to the webroot and start it

```bash
docker-compose up --build web
```
You should now be able to navigate to [http://localhost:5000](http://localhost:5000) and use the application.
