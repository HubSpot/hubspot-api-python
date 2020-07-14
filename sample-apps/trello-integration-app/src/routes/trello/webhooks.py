from http import HTTPStatus
from flask import Blueprint


module = Blueprint("trello.webhooks", __name__)


@module.route("/handle", methods=["POST", "GET"])
def handle():
    return "", HTTPStatus.NO_CONTENT
