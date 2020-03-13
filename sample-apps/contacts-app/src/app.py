from flask import Flask, redirect

import routes

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(routes.oauth, url_prefix='/oauth')
app.register_blueprint(routes.contacts, url_prefix='/contacts')
app.register_blueprint(routes.properties, url_prefix='/properties')


@app.route('/')
def contacts():
    return redirect('/contacts')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
