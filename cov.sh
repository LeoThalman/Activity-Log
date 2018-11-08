#!/usr/bin/env bash
cp test.settings .env
coverage run --source "." -m py.test
coverage html
firefox htmlcov/index.html
