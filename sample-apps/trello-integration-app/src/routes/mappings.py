from flask import Blueprint, render_template, request, redirect, url_for
from auth import auth_required
from helpers.trello import get_client
from helpers.hubspot import create_client
from services.db import session, Mapping

module = Blueprint("mappings", __name__)


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
        "mappings/pipelines.html",
        board_id=board_id,
        pipelines=pipelines.results
    )


@module.route("/boards/<board_id>/pipelines/<pipeline_id>", methods=["GET"])
@auth_required
def list(board_id, pipeline_id):
    trello = get_client()
    board = trello.get_board(board_id)
    board_lists = board.list_lists()

    hubspot = create_client()
    pipeline = hubspot.crm.pipelines.pipelines_api.get_by_id("deals", pipeline_id)

    mappings = session.query(Mapping).filter_by(
        board_id=board_id,
        pipeline_id=pipeline_id,
    ).all()
    session.commit()

    return render_template(
        "mappings/list.html",
        mappings=mappings,
        board=board,
        board_lists=board_lists,
        pipeline=pipeline,
    )


@module.route("/boards/<board_id>/pipelines/<pipeline_id>", methods=["POST"])
@auth_required
def save(board_id, pipeline_id):
    mappings_fields = {
        "board_list_id": request.form.getlist("board_list_ids[]"),
        "pipeline_stage_id": request.form.getlist("pipeline_stage_id[]")
    }
    for field_name, fields in mappings_fields.items():
        for field_encoded in fields:
            mapping_id, field_value = field_encoded.split("_")
            mapping = session.query(Mapping).get(mapping_id)
            setattr(mapping, field_name, field_value)
    session.commit()

    return redirect(url_for("mappings.list", board_id=board_id, pipeline_id=pipeline_id))


@module.route("/boards/<board_id>/pipelines/<pipeline_id>/add-row", methods=["GET"])
@auth_required
def add_row(board_id, pipeline_id):
    mapping = Mapping()
    mapping.board_id = board_id
    mapping.pipeline_id = pipeline_id
    session.add(mapping)
    session.commit()

    return redirect(url_for("mappings.list", board_id=board_id, pipeline_id=pipeline_id))


@module.route("/boards/<board_id>/pipelines/<pipeline_id>/delete/<mapping_id>", methods=["GET"])
@auth_required
def delete_row(board_id, pipeline_id, mapping_id):
    mapping = session.query(Mapping).get(mapping_id)
    session.delete(mapping)
    session.commit()

    return redirect(url_for("mappings.list", board_id=board_id, pipeline_id=pipeline_id))
