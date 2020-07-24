import json
from http import HTTPStatus
from flask import Blueprint, request
from hubspot.crm.deals import SimplePublicObjectInput
from repositories import AssociationsRepository
from helpers.hubspot import create_client
from services.db import session, Mapping


module = Blueprint("trello.webhooks", __name__)


@module.route("/handle", methods=["GET"])
def head():
    return "", HTTPStatus.OK


@module.route("/handle", methods=["POST"])
def handle():
    data = json.loads(request.data)
    # handle only "list" change event
    if "listAfter" in data["action"]["data"]:
        board_list_id = data["action"]["data"]["listAfter"]["id"]
        card_id = data["model"]["id"]
        associations = AssociationsRepository.find_by_card_id(card_id)
        hubspot = create_client()
        for association in associations:
            deal_id = association.deal_id
            deal = hubspot.crm.deals.basic_api.get_by_id(deal_id)
            mapping = (
                session.query(Mapping)
                .filter_by(
                    board_list_id=board_list_id,
                    pipeline_id=deal.properties["pipeline"],
                )
                .first()
            )
            session.commit()
            if mapping is not None:
                simple_public_object_input = SimplePublicObjectInput(
                    properties={"dealstage": mapping.pipeline_stage_id},
                )
                hubspot.crm.deals.basic_api.update(
                    deal_id=deal_id,
                    simple_public_object_input=simple_public_object_input,
                )

    return "", HTTPStatus.OK
