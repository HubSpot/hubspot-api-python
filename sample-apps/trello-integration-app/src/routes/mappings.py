from flask import Blueprint, render_template, request, redirect, url_for
from auth import auth_required
from helpers.trello import get_client
from helpers.hubspot import create_client
from services.db import Mapping
from repositories import MappingsRepository

module = Blueprint("mappings", __name__)

JOIN_SEPARATOR = "#"


@module.route("/", methods=["GET"])
@auth_required
def home():
    return redirect(url_for("mappings.boards_list"))


@module.route("/boards", methods=["GET"])
@auth_required
def boards_list():
    trello = get_client()
    trello_boards = trello.list_boards()

    return render_template(
        "mappings/boards.html",
        trello_boards=trello_boards,
    )


@module.route("/boards/<board_id>/pipelines", methods=["GET"])
@auth_required
def pipelines_list(board_id):
    hubspot = create_client()
    pipelines = hubspot.crm.pipelines.pipelines_api.get_all("deals")

    return render_template(
        "mappings/pipelines.html", board_id=board_id, pipelines=pipelines.results
    )


@module.route("/boards/<board_id>/pipelines/<pipeline_id>", methods=["GET"])
@auth_required
def list(board_id, pipeline_id):
    trello = get_client()
    board = trello.get_board(board_id)
    board_lists = board.list_lists()

    hubspot = create_client()
    pipeline = hubspot.crm.pipelines.pipelines_api.get_by_id("deals", pipeline_id)

    mappings = MappingsRepository.find_by(
        board_id=board_id,
        pipeline_id=pipeline_id,
    )
    mappings.append(
        {
            "id": None,
            "board_list_id": None,
            "pipeline_stage_id": None,
        }
    )

    return render_template(
        "mappings/list.html",
        mappings=mappings,
        board=board,
        board_lists=board_lists,
        pipeline=pipeline,
        JOIN_SEPARATOR=JOIN_SEPARATOR,
    )


@module.route("/boards/<board_id>/pipelines/<pipeline_id>", methods=["POST"])
@auth_required
def save(board_id, pipeline_id):
    mappings_fields = {
        "board_list_id": request.form.getlist("board_list_ids[]"),
        "pipeline_stage_id": request.form.getlist("pipeline_stage_id[]"),
    }
    new_mapping = Mapping()
    new_mapping.board_id = board_id
    new_mapping.pipeline_id = pipeline_id
    for field_name, fields in mappings_fields.items():
        for field_encoded in fields:
            mapping_id, field_value = field_encoded.split(JOIN_SEPARATOR)
            if mapping_id == "None":
                setattr(new_mapping, field_name, field_value)
            else:
                mapping = MappingsRepository.get(mapping_id)
                setattr(mapping, field_name, field_value)
                MappingsRepository.save(mapping)

    if (
        new_mapping.board_list_id is not None
        or new_mapping.pipeline_stage_id is not None
    ):
        MappingsRepository.save(new_mapping)

    return redirect(
        url_for("mappings.list", board_id=board_id, pipeline_id=pipeline_id)
    )


@module.route(
    "/boards/<board_id>/pipelines/<pipeline_id>/delete/<mapping_id>", methods=["GET"]
)
@auth_required
def delete_row(board_id, pipeline_id, mapping_id):
    MappingsRepository.delete_by_id(mapping_id)

    return redirect(
        url_for("mappings.list", board_id=board_id, pipeline_id=pipeline_id)
    )
