from flask import Flask, jsonify, abort, request, url_for
from datetime import datetime
from mongoengine import *
from bson import ObjectId
import os
import json

app = Flask(__name__)
connect(db=os.environ.get('ACTLOG_DB'), host='localhost')

def setup_tests():
    logs = ActivityLog.objects
    for log in logs:
        log.delete()
    recordOne = ActivityLog(
        user_id= 0,
        username= "frank",
        details= "stuff here"
        ).save()
    recordTwo = ActivityLog(
        user_id= 1,
        username= "zeet",
        details= "different stuff here"
        ).save()

class ActivityLog(Document):
    user_id = IntField(required=True)
    username = StringField(required=True, max_length=64)
    timestamp = DateTimeField(default=datetime.utcnow())
    details = StringField(required=True)

    @queryset_manager
    def objects(doc_cls, queryset):
        return queryset.order_by('-timestamp')



@app.route("/api/activities/<string:id>", methods=["GET"])
def activity(id):
    log_id = ObjectId(id)
    log = ActivityLog.objects(id=log_id).first()
    if log == None:
        abort(404)
    rtn = json.loads(log.to_json())
    return jsonify(rtn)

@app.route("/api/activities/", methods=["GET"])
def activities():
    logs = ActivityLog.objects[:10]
    rtn =  {"activities" : json.loads(logs.to_json())}
    return jsonify(rtn)

@app.route("/api/activities", methods=["POST"])
def new_activity():
    if not request.json:
        abort(400)
    new_log = request.get_json()
    if "user_id" not in new_log or "username" not in new_log or "details" not in new_log:
        abort(400)
    log = ActivityLog(
            user_id=new_log["user_id"],
            username=new_log["username"],
            details=new_log["details"]).save()
    log_id = str(log.id)
    rtn = json.loads(log.to_json())
    rtn["location"] = url_for("activity", id=rtn["_id"]["$oid"])

    return jsonify(rtn), 201
