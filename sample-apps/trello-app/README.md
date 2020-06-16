# HubSpot-python sample Trello app

This is a sample app for the hubspot-python SDK. Currently, this app focuses on demonstrating
of Trello integration, Trello cards and HubSpot deals in particular.

### Setup App

Make sure you have [Docker Compose](https://docs.docker.com/compose/) installed.

### Configure

1. Copy .env.template to .env
2. Paste your HUBSPOT_CLIENT_ID and HUBSPOT_CLIENT_SECRET

### Running

The best way to run this project (with the least configuration), is using docker compose.  Change to the webroot and start it

```bash
docker-compose up --build
```
You should now be able to navigate to [http://localhost:5000](http://localhost:5000) and use the application.
