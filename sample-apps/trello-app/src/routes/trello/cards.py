import os
import http
from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from helpers.trello import search_cards, get_client, get_search_query, save_search_query
from helpers.associations import (
    is_deal_associated, create_deal_association, get_deal_association, delete_deal_association
)
from formatters.trello.cards import format_card_extension_data_response


module = Blueprint("trello.cards", __name__)


@module.route("/search_query", methods=["GET"])
def search_query():
    query = get_search_query()
    return render_template("trello/cards/search_query.html", search_query=query)


@module.route("/search_query", methods=["POST"])
def update_search_query():
    print(request.form, flush=True)
    query = request.form.get("search_query")
    save_search_query(query)
    return redirect(url_for("trello.cards.search_query"))


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
        query = get_search_query()
        cards = search_cards(search_query=query)
    else:
        card_id = get_deal_association(deal_id)
        trello = get_client()
        cards = [trello.get_card(card_id=card_id)]
    response = format_card_extension_data_response(
        deal_associated=deal_associated,
        cards=cards
    )

    return jsonify(response)
