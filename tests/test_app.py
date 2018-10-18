import pytest
from flask import Flask, url_for
import sys
sys.path.append('..')
import app
import requests



def test_activity_errors_on_invalid_id(client, setup_module):
    response = client.get(url_for("activity", id='aaaaaaaaaaaaaaaaaaaaaaaa'))
    assert response.status_code == 404

def test_activities_returns_json(client, setup_module):
    response = client.get(url_for("activities"))
    assert response.status_code == 200
    data = response.get_json()
    doc1 = data["activities"][0]["username"]
    doc2 = data["activities"][1]["username"]
    assert (doc1 == "zeet") or (doc2 == "zeet")

def test_activity_returns_json_on_valid_id(client, setup_module):
    id_response = client.get(url_for("activities"))
    data = id_response.get_json()
    log_id = str(data["activities"][0]["_id"])
    response = client.get(url_for("activity", id=log_id))
    assert response.status_code == 200
    r_data = response.get_json()
    assert r_data["username"] == data["activities"][0]["username"]

def test_post_activity_should_fail_with_no_json(client, setup_module):
    response = client.post(url_for('new_activity'))
    assert response.status_code == 400

def test_post_activity_should_fail_with_incorrect_json(client, setup_module):
    response = client.post(url_for('new_activity'),
        json=dict(
            username="tony",
            user_id="2"
        ))
    assert response.status_code == 400
