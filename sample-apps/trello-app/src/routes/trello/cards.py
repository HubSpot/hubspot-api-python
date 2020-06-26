import http
from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from helpers.trello import search_cards, get_client
from helpers.associations import (
    is_deal_associated, create_deal_association, get_deal_association, delete_deal_association
)
from formatters.trello.cards import format_card_extension_data_response


module = Blueprint("trello.cards", __name__)


@module.route("/search")
def search():
    query = request.args.get("q")
    cards = search_cards(query=query)
    response = [{
        "name": card.name,
        "id": card.id,
    } for card in cards]

    return jsonify(response)


@module.route("/search_frame", methods=["GET"])
def search_frame():
    return render_template("trello/cards/search_frame.html")


@module.route("/search_frame", methods=["POST"])
def create_association():
    deal_id = request.args.get("hs_object_id")
    card_id = request.form.get("card_id")
    create_deal_association(deal_id, card_id)
    return redirect(url_for("trello.cards.search_frame_success"))


@module.route("/search_frame_success", methods=["GET"])
def search_frame_success():
    return render_template("trello/cards/search_frame_success.html")


@module.route("/association", methods=["DELETE"])
def delete_association():
    deal_id = request.args.get("hs_object_id")
    delete_deal_association(deal_id)
    return "", http.HTTPStatus.NO_CONTENT


@module.route("/")
def card_extension_data():
    deal_id = request.args["hs_object_id"]
    deal_associated = is_deal_associated(deal_id)
    cards = []
    if deal_associated:
        card_id = get_deal_association(deal_id)
        trello = get_client()
        cards = [trello.get_card(card_id=card_id)]
    response = format_card_extension_data_response(
        deal_associated=deal_associated,
        cards=cards
    )

    return jsonify(response)
