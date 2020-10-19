from flask import url_for


def format_card_extension_data_response(deal_associated, card=None):
    if deal_associated:
        result = {
            "objectId": card.short_id,
            "title": card.name,
            "link": card.short_url,
        }
        if len(card.members) > 0:
            result["properties"] = [
                {
                    "label": "Members",
                    "dataType": "STRING",
                    "value": ", ".join([member.username for member in card.members]),
                }
            ]
        results = [result]
        primary_action = {
            "type": "ACTION_HOOK",
            "httpMethod": "DELETE",
            "associatedObjectProperties": [
                "hs_object_id",
            ],
            "uri": url_for("trello.associations.delete_association", _external=True),
            "label": "Remove the association",
        }
    else:
        results = []
        primary_action = {
            "type": "IFRAME",
            "width": 650,
            "height": 350,
            "uri": url_for("trello.associations.search_frame", _external=True),
            "label": "Associate Trello card",
            "associatedObjectProperties": [
                "hs_object_id",
                "dealname",
            ],
        }

    return {
        "results": results,
        "primaryAction": primary_action,
    }
