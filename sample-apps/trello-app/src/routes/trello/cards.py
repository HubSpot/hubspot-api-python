import os
from flask import Blueprint, jsonify
from helpers.trello import fetch_cards


module = Blueprint("trello.cards", __name__)


@module.route("/")
def fetch():
    board_name = os.getenv("TRELLO_BOARD_NAME")
    cards_limit = int(os.getenv("TRELLO_CARDS_LIMIT"))
    cards = fetch_cards(board_name, cards_limit)
    data = {
        "results": [
            {
                "objectId": card.short_id,
                "title": card.name,
                "link": card.short_url,
                "actions": [
                    {
                        "type": "ACTION_HOOK",
                        "httpMethod": "PUT",
                        "associatedObjectProperties": [],
                        "uri": "https://example.com",
                        "label": "Assign"
                    },
                ],
            } for card in cards
        ],
    }

    return jsonify(data)
