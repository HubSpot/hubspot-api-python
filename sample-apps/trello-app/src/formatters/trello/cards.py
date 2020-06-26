from flask import url_for


def format_card_extension_data_response(deal_associated, cards):
    results = []
    for card in cards:
        result = {
            "objectId": card.short_id,
            "title": card.name,
            "link": card.short_url,

        }
        results.append(result)
    response = {
        "results": results
    }
    if deal_associated:
        response["primaryAction"] = {
            "type": "ACTION_HOOK",
            "httpMethod": "DELETE",
            "associatedObjectProperties": [
                "hs_object_id", "label",
            ],
            "uri": url_for("trello.cards.delete_association", _external=True),
            "label": "Remove association",
        }
    else:
        response["primaryAction"] = {
            "type": "IFRAME",
            "width": 550,
            "height": 300,
            "uri": url_for("trello.cards.search_frame", _external=True),
            "label": "Associate",
            "associatedObjectProperties": [
                "hs_object_id", "label",
            ],
        }

    return response
