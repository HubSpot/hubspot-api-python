import json
import tempfile
import os
from flask import Blueprint, render_template, request, redirect, url_for
from auth import auth_required
from helpers.hubspot import create_client


module = Blueprint("imports", __name__)


@module.route("/")
@auth_required
def list():
    hubspot = create_client()
    imports_page = hubspot.crm.imports.core_api.get_page()
    return render_template("imports/list.html", imports=imports_page.results)


@module.route("/<import_id>")
@auth_required
def show(import_id):
    hubspot = create_client()
    import_data = hubspot.crm.imports.core_api.get_by_id(import_id)
    return render_template("imports/show.html", import_data=import_data)


@module.route("/new")
@auth_required
def new():
    return render_template("imports/new.html")


@module.route("/start", methods=["POST"])
@auth_required
def start():
    file = request.files["file"]

    handle, filepath = tempfile.mkstemp(suffix=".csv")
    os.close(handle)
    file.save(filepath)

    import_request = {
        "name": "Import '{}'".format(file.filename),
        "files": [
            {
                "fileName": os.path.basename(filepath),
                "fileImportPage": {
                    "hasHeader": True,
                    "columnMappings": [
                        {
                            "columnName": "First Name",
                            "propertyName": "firstname",
                            "columnObjectType": "CONTACT",
                        },
                        {
                            "columnName": "Email",
                            "propertyName": "email",
                            "columnObjectType": "CONTACT",
                        },
                    ],
                },
            }
        ],
    }
    hubspot = create_client()
    import_data = hubspot.crm.imports.core_api.create(
        files=filepath, import_request=json.dumps(import_request)
    )

    os.unlink(filepath)

    return redirect(url_for("imports.show", import_id=import_data.id))
