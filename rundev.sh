#!/usr/bin/env bash
export ACTLOG_DB='activity-log'
export FLASK_APP=app.py
export FLASK_ENV=development

flask run --host=0.0.0.0 --port 5001
