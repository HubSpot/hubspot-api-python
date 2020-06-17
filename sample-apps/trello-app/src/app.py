from flask import Flask, redirect, url_for
from helpers.reverse_proxied import ReverseProxied
import routes

app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(routes.oauth, url_prefix="/oauth")
app.register_blueprint(routes.trello, url_prefix="/trello")


@app.route("/")
def home():
    return redirect(url_for("oauth.login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
