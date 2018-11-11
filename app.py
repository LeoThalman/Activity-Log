from flask import Flask, jsonify, abort, request, url_for
from datetime import datetime
from mongoengine import *
from dotenv import load_dotenv
from bson import ObjectId
import os
import json

app = Flask(__name__)


load_dotenv(override=True)

mongo_host = os.getenv('DB_HOST')
mongo_db = os.getenv('ACTLOG_DB')
mongo_user = os.getenv('DB_USER')
mongo_password = os.getenv('DB_PASSWORD')

connect(db=mongo_db,
        host=mongo_host,
        username=mongo_user,
        password=mongo_password
        )



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
    rtn = json.loads(log.to_json())
    rtn["id"] = str(rtn["_id"]["$oid"])
    rtn["location"] = url_for("activity", id=str(rtn["_id"]["$oid"]))
    rtn.pop("_id")

    return jsonify(rtn), 201
