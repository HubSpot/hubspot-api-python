from flask import Flask, render_template

import routes

app = Flask(__name__)
app.register_blueprint(routes.oauth)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
