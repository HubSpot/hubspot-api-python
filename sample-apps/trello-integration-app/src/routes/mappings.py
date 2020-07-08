from flask import Blueprint, render_template
from auth import auth_required
from helpers.trello import get_client
from helpers.hubspot import create_client

module = Blueprint("mappings", __name__)


@module.route("/", methods=["GET"])
@auth_required
def boards_list():
    trello = get_client()
    trello_boards = trello.list_boards()

    return render_template(
        "mappings/boards.html",
        trello_boards=trello_boards,
    )


@module.route("/board/<board_id>", methods=["GET"])
@auth_required
def pipelines_list(board_id):
    hubspot = create_client()
    pipelines = hubspot.crm.pipelines.pipelines_api.get_all("deals")

    return render_template(
        "mappings/pipelines.html",
        board_id=board_id,
        pipelines=pipelines.results
    )


@module.route("/board/<board_id>/pipeline/<pipeline_id>", methods=["GET"])
@auth_required
def list(board_id, pipeline_id):
    trello = get_client()
    board = trello.get_board(board_id)
    board_lists = board.list_lists()

    hubspot = create_client()
    pipeline = hubspot.crm.pipelines.pipelines_api.get_by_id("deals", pipeline_id)

    return render_template(
        "mappings/list.html",
        board=board,
        board_lists=board_lists,
        pipeline=pipeline,
    )
