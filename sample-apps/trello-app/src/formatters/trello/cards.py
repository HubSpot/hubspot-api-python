from flask import url_for


def format_card_extension_data_response(deal_associated, cards):
    results = []
    for card in cards:
        result = {
            "objectId": card.short_id,
            "title": card.name,
            "link": card.short_url,

        }
        if not deal_associated:
            result["actions"] = [
                {
                    "type": "ACTION_HOOK",
                    "httpMethod": "GET",
                    "associatedObjectProperties": [
                        "hs_object_id", "dealname", "dealstage"
                    ],
                    "uri": url_for("trello.cards.create_association", card_id=card.id, _external=True),
                    "label": "Assign To Deal",
                },
            ]
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
            "label": "Remove Association",
        }

    return response
