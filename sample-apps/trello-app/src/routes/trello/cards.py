import os
import http
from flask import Blueprint, jsonify, request
from helpers.trello import fetch_cards, get_client
from helpers.associations import (
    is_deal_associated, create_deal_association, get_deal_association, delete_deal_association
)
from formatters.trello.cards import format_card_extension_data_response


module = Blueprint("trello.cards", __name__)


@module.route("/<card_id>/association", methods=["POST"])
def create_association(card_id):
    deal_id = request.form.get("hs_object_id")
    create_deal_association(deal_id, card_id)
    return "", http.HTTPStatus.NO_CONTENT


@module.route("/association", methods=["DELETE"])
def delete_association():
    deal_id = request.args.get("hs_object_id")
    delete_deal_association(deal_id)
    return "", http.HTTPStatus.NO_CONTENT


@module.route("/")
def card_extension_data():
    deal_id = request.args["hs_object_id"]
    deal_associated = is_deal_associated(deal_id)
    if not deal_associated:
        board_name = os.getenv("TRELLO_BOARD_NAME")
        cards_limit = int(os.getenv("TRELLO_CARDS_LIMIT"))
        cards = fetch_cards(board_name, cards_limit)
    else:
        card_id = get_deal_association(deal_id)
        trello = get_client()
        cards = [trello.get_card(card_id=card_id)]
    response = format_card_extension_data_response(
        deal_associated=deal_associated,
        cards=cards
    )

    return jsonify(response)
