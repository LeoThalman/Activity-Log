from flask import Flask, jsonify, abort, request, url_for
from datetime import datetime

app = Flask(__name__)

siamese = {"breed": "Siamese", "style": "Feisty"}

persian = {"breed": "Persian", "style": "Ambivalent"}

catbreed_list = [siamese, persian]

activity_log = [
    {
        'id': 0,
        'user_id': 1,
        'username': 'john',
        'timestamp': datetime.utcnow(),
        'details': "Important stuff here",
    },
    {
        'id': 1,
        'user_id': 2,
        'username': 'yoko',
        'timestamp': datetime.utcnow(),
        'details': "Even more important",
    },
]


@app.route("/api/activities/<int:id>", methods=["GET"])
def activity(id):
    if id < 0 or id >= len(activity_log):
        abort(404)
    return jsonify(activity_log[id])


@app.route("/api/activities/", methods=["GET"])
def activities():
    return jsonify({"activities": activity_log})


@app.route("/api/catbreeds", methods=["POST"])
def new_catbreed():
    if not request.json:
        abort(400)
    new_breed = request.get_json()
    if "breed" not in new_breed or "style" not in new_breed:
        abort(400)
    new_breed["id"] = 999
    new_breed["location"] = url_for("catbreed", id=999)
    return jsonify(new_breed)
