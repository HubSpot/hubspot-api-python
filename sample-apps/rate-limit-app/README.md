# HubSpot-python sample Rate Limit App

This is a sample app for the [hubspot-python SDK](../../../..). Currently, this app focuses on demonstrating the rate limit mechanism. It will be useful for you if you often reach rate limit (429 http error).

The application uses https://pypi.org/project/redis-ratelimit/ package.
Please check [worker.py](./src/worker.py) on how to specify rate limit in in your application to avoid 429 http errors.

Please see the documentation on [Creating an app in HubSpot](https://developers.hubspot.com/docs/creating-an-app)

### HubSpot Public API endpoints used in this application

  - [Contacts](https://developers.hubspot.com/docs/crm/contacts)
  - [OAuth](https://developers.hubspot.com/docs/working-with-oauth)

### Setup App

Make sure you have [Docker Compose](https://docs.docker.com/compose/) installed.

### Configure

1. Copy .env.template to .env
2. Specify authorization data in .env:
    - Paste HUBSPOT_CLIENT_ID and HUBSPOT_CLIENT_SECRET for OAuth

### Running

The best way to run this project (with the least configuration), is using docker compose.  Change to the webroot and start it

```bash
docker-compose up --build
```
You should now be able to navigate to [http://localhost:8999](http://localhost:5000).
Firstly you will need to authorize via OAuth there.
Than you can to go to the terminal window and start the following command in the application root

```bash
docker-compose exec web python worker.py
```
