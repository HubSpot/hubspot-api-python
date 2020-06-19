import os
import http
from flask import Blueprint, jsonify, request, url_for
from helpers.trello import fetch_cards, get_client
from helpers.associations import is_deal_associated, associate_deal, get_deal_association, remove_deal_association


module = Blueprint("trello.cards", __name__)


@module.route("/<card_id>/association", methods=["GET"])
def associate(card_id):
    deal_id = request.args.get("hs_object_id")
    associate_deal(deal_id, card_id)
    return "", http.HTTPStatus.NO_CONTENT


@module.route("/association", methods=["DELETE"])
def remove_association():
    deal_id = request.args.get("hs_object_id")
    remove_deal_association(deal_id)
    return "", http.HTTPStatus.NO_CONTENT


@module.route("/")
def card_extension_data():
    deal_id = request.args["hs_object_id"]
    if not is_deal_associated(deal_id):
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
                            "httpMethod": "GET",
                            "associatedObjectProperties": [
                                "hs_object_id", "dealname", "dealstage"
                            ],
                            "uri": url_for("trello.cards.associate", card_id=card.id, _external=True),
                            "label": "Assign To Deal",
                        },
                    ],
                } for card in cards
            ],
        }
    else:
        card_id = get_deal_association(deal_id)
        print(card_id, type(card_id), flush=True)
        trello = get_client()
        card = trello.get_card(card_id=card_id)
        data = {
            "results": [
                {
                    "objectId": card.short_id,
                    "title": card.name,
                    "link": card.short_url,
                },
            ],
            "primaryAction": {
                "type": "ACTION_HOOK",
                "httpMethod": "DELETE",
                "associatedObjectProperties": [
                    "hs_object_id", "label",
                ],
                "uri": url_for("trello.cards.remove_association", _external=True),
                "label": "Remove Association",
            },
        }

    return jsonify(data)
