from flask import Flask, jsonify, abort, request, url_for
from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client["activity-log"]

@app.route("/api/activities/<string:id>", methods=["GET"])
def activity(id):
    log_id = ObjectId(id)
    rtn = db["act_log"].find_one({"_id": log_id})
    if rtn == None:
        abort(404)
    rtn["_id"] = str(rtn["_id"])
    return jsonify(rtn)

@app.route("/api/activities/", methods=["GET"])
def activities():
    act_log = db["act_log"]
    rtn = list(act_log.find({}).sort("timestamp").limit(10))
    for log in rtn:
        log["_id"] = str(log["_id"])
    return jsonify({"activities": rtn})

@app.route("/api/activities", methods=["POST"])
def new_activity():
    act_log = db["act_log"]
    if not request.json:
        abort(400)
    new_act_log = request.get_json()
    if "user_id" not in new_act_log or "username" not in new_act_log or "details" not in new_act_log:
        abort(400)
    new_act_log["timestamp"] = datetime.utcnow()
    log_id = str(act_log.insert_one(new_act_log).inserted_id)
    rtn = dict(new_act_log)
    rtn["_id"] = str(log_id)
    rtn["location"] = url_for("activity", id=rtn["_id"])
    return jsonify(rtn), 201
