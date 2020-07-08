from flask import Flask, redirect, url_for

import routes

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(routes.oauth, url_prefix="/oauth")
app.register_blueprint(routes.companies, url_prefix="/companies")
app.register_blueprint(routes.mappings, url_prefix="/associations")


@app.route("/")
def index():
    return redirect(url_for("companies.list"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
