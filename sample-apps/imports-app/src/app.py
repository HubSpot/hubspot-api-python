from flask import Flask, redirect, url_for

import routes

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(routes.oauth, url_prefix="/oauth")
app.register_blueprint(routes.imports, url_prefix="/imports")


@app.route("/")
def main():
    return redirect(url_for("imports.new"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
