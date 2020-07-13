import http
from flask import Blueprint


module = Blueprint("trello.webhooks", __name__)


@module.route("/handle", methods=["POST", "GET"])
def handle():
    return "", http.HTTPStatus.NO_CONTENT
