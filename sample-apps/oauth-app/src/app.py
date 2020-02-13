from flask import Flask

import routes

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(routes.oauth)
app.register_blueprint(routes.contacts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
