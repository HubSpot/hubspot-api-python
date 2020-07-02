# HubSpot-python sample Trello integration app

This is a sample app for the hubspot-python SDK. Currently, this app focuses on demonstrating
of Trello integration, Trello cards and HubSpot deals in particular.

### HubSpot Public API links used in this application

- [CRM Custom Cards](https://developers.hubspot.com/docs/api/crm/extensions/custom-cards)

### Setup App

Make sure you have [Docker Compose](https://docs.docker.com/compose/) installed.

### Configure

1. Copy .env.template to .env
2. Paste your HUBSPOT_CLIENT_ID, HUBSPOT_CLIENT_SECRET, HUBSPOT_APPLICATION_ID and HUBSPOT_DEVELOPER_API_KEY
3. Paste you TRELLO_API_KEY. You can obtain it from [https://trello.com/app-key](https://trello.com/app-key)

### Running

The best way to run this project (with the least configuration), is using docker compose.  Change to the webroot and start it

```bash
docker-compose up --build
```

Copy Ngrok url from console. Now you should now be able to navigate to that url and use the application.
