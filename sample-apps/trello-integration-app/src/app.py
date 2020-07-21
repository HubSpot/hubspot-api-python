from flask import Flask, redirect, url_for
from helpers.reverse_proxied import ReverseProxied
from services.db import create_db_schema
from routes.oauth import module as routes_oauth
from routes.init import module as routes_init
from routes.trello.auth import module as routes_trello_auth
from routes.trello.associations import module as routes_trello_cards
from routes.trello.webhooks import module as routes_trello_webhooks
from routes.mappings import module as routes_mappings

app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

create_db_schema()

app.register_blueprint(routes_oauth, url_prefix="/oauth")
app.register_blueprint(routes_init, url_prefix="/init")
app.register_blueprint(routes_trello_auth, url_prefix="/trello/auth")
app.register_blueprint(routes_trello_cards, url_prefix="/trello/cards")
app.register_blueprint(routes_trello_webhooks, url_prefix="/trello/webhooks")
app.register_blueprint(routes_mappings, url_prefix="/mappings")


@app.route("/")
def home():
    return redirect(url_for("init.extension"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
