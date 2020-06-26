from flask import url_for


def format_card_extension_data_response(deal_associated, card=None):
    if deal_associated:
        results = [{
            "objectId": card.short_id,
            "title": card.name,
            "link": card.short_url,
        }]
        primary_action = {
            "type": "ACTION_HOOK",
            "httpMethod": "DELETE",
            "associatedObjectProperties": [
                "hs_object_id",
            ],
            "uri": url_for("trello.cards.delete_association", _external=True),
            "label": "Remove the association",
        }
    else:
        results = []
        primary_action = {
            "type": "IFRAME",
            "width": 650,
            "height": 350,
            "uri": url_for("trello.cards.search_frame", _external=True),
            "label": "Associate Trello card",
            "associatedObjectProperties": [
                "hs_object_id", "dealname",
            ],
        }

    return {
        "results": results,
        "primaryAction": primary_action,
    }
