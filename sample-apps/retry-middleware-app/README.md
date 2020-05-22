# HubSpot-python sample Retry Middleware App

This is a sample app for the [hubspot-python SDK](../../../..). Currently, this app focuses on demonstrating the retry middleware. It will be useful for you if you often reach rate limit (429 http error).

The application uses [urllib3.util package](https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html).
Please check [worker.py](./src/worker.py) on how to specify retry middleware in your application.

Please see the documentation on [Creating an app in HubSpot](https://developers.hubspot.com/docs-beta/creating-an-app)

### HubSpot Public API endpoints used in this application

  - [Contacts](https://developers.hubspot.com/docs-beta/crm/contacts)
  - [OAuth](https://developers.hubspot.com/docs-beta/working-with-oauth)

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
You should now be able to navigate to [http://localhost:5000](http://localhost:5000).
Firstly you will need to authorize via OAuth there.
Than you can to go to the terminal window and start the following command in the application root

```bash
docker-compose exec web python worker.py
```
