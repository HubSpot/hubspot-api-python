import json
import tempfile
import os
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
from auth import auth_required
from helpers.hubspot import create_client


module = Blueprint("imports", __name__)


@module.route("/")
@auth_required
def readme():
    return render_template("imports/readme.html")


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
        ]
    }
    hubspot = create_client()
    response = hubspot.crm.imports.core_api.create(files=filepath, import_request=json.dumps(import_request))

    os.unlink(filepath)
    return render_template("imports/result.html", response=response)

