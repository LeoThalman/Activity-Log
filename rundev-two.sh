#!/usr/bin/env bash
cp dev.settings .env

flask run --host=0.0.0.0 --port 5002
