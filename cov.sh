/#!/usr/bin/env bash
export ACTLOG_DB='activity-log-tests'
coverage run --source "." -m py.test
coverage html
firefox htmlcov/index.html
