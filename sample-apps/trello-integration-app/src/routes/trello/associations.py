import http
from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from helpers.trello import search_cards, get_client, create_webhook, update_webhook
from formatters.trello.cards import format_card_extension_data_response
from auth import hubspot_signature_required
from repositories import AssociationsRepository, WebhooksRepository


module = Blueprint("trello.associations", __name__)


@module.route("/search")
def search():
    query = request.args.get("q")
    cards = search_cards(query=query)
    response = [{"name": card.name, "id": card.id} for card in cards]

    return jsonify(response)


@module.route("/search_frame", methods=["GET"])
def search_frame():
    deal_name = request.args.get("dealname")
    return render_template("trello/cards/search_frame.html", deal_name=deal_name)


@module.route("/search_frame", methods=["POST"])
def create_association():
    deal_id = request.args.get("hs_object_id")
    card_id = request.form.get("card_id")
    AssociationsRepository.create(deal_id, card_id)
    callback_url = url_for("trello.webhooks.handle", _external=True)
    webhooks = WebhooksRepository.find_by(card_id=card_id)
    if len(webhooks) > 0:
        for webhook in webhooks:
            update_webhook(webhook_id=webhook.webhook_id, callback_url=callback_url)
            webhook.url = callback_url
            WebhooksRepository.save(webhook)
    else:
        webhook_data = create_webhook(callback_url=callback_url, card_id=card_id)
        WebhooksRepository.create(
            webhook_id=webhook_data["id"],
            card_id=card_id,
            url=callback_url,
        )

    return redirect(url_for("trello.associations.search_frame_success"))


@module.route("/search_frame_success", methods=["GET"])
def search_frame_success():
    return render_template("trello/cards/search_frame_success.html")


@module.route("/", methods=["DELETE"])
@hubspot_signature_required
def delete_association():
    deal_id = request.args.get("hs_object_id")
    AssociationsRepository.delete_by_deal_id(deal_id)
    return "", http.HTTPStatus.NO_CONTENT


@module.route("/card_extension")
@hubspot_signature_required
def card_extension_data():
    deal_id = request.args["hs_object_id"]
    deal_associated = AssociationsRepository.is_deal_associated(deal_id)
    card = None
    if deal_associated:
        association = AssociationsRepository.find_one_by_deal_id(deal_id)
        trello = get_client()
        card = trello.get_card(card_id=association.card_id)
        card.members = [trello.get_member(m) for m in card.idMembers]
    response = format_card_extension_data_response(
        deal_associated=deal_associated, card=card
    )

    return jsonify(response)
