from flask import Flask, jsonify, abort, request, url_for
from datetime import datetime

app = Flask(__name__)

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


@app.route("/api/activities", methods=["POST"])
def new_activity():
    if not request.json:
        abort(400)
    new_act_log= request.get_json()
    if "user_id" not in new_act_log or "username" not in new_act_log or "details" not in new_act_log:
        abort(400)
    new_act_log["id"] = len(activity_log)
    new_act_log["timestamp"] = datetime.utcnow()
    activity_log.append(new_act_log)
    rtn = dict(new_act_log)
    rtn["location"] = url_for("activity", id=new_act_log["id"])
    return jsonify(rtn)
