from flask import Blueprint

module = Blueprint("trello.cards", __name__)


@module.route("/")
def fetch():
    pass
