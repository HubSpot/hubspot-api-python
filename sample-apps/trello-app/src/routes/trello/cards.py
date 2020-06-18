import os
from flask import Blueprint, jsonify
from helpers.trello import get_client


module = Blueprint("trello.cards", __name__)


@module.route("/")
def fetch():
    client = get_client()

    all_boards = client.list_boards()
    board_name = os.getenv("TRELLO_BOARD_NAME")
    board = next((board for board in all_boards if board.name.lower() == board_name.lower()), None)

    cards_limit = int(os.getenv("TRELLO_CARDS_LIMIT"))
    cards = []
    for list in board.list_lists():
        if len(cards) >= cards_limit:
            break
        for card in list.list_cards():
            cards.append(card)
            if len(cards) >= cards_limit:
                break

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
