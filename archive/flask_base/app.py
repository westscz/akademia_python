from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello_world"


@app.route("/data", methods=["PUT"])
def data_path():
    import json

    if request.is_json:
        return json.dumps({"data": request.json, "status_code": 200}), 200
    else:
        return json.dumps({"status_code": 400}), 400


@app.route("/<name>")
def hello_you(name):
    return f"hello_{name}"


@app.route("/<get>/<some>/<arguments>")
def path_args(**kwargs):
    return f"path_args:{kwargs} query:{request.query_string}"
