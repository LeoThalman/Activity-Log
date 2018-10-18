/#!/usr/bin/env bash

coverage run --source "." -m py.test
coverage html
firefox htmlcov/index.html
