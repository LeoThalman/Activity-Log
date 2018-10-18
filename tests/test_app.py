import pytest
from flask import Flask, url_for
import sys
sys.path.append('..')
import app
import requests

def test_activity_errors_on_invalid_id(client):
    response = client.get(url_for("activity", id='aaaaaaaaaaaaaaaaaaaaaaaa'))
    assert response.status_code == 404

def test_activities_returns_json(client):
    response = client.get(url_for("activities"))
    assert response.status_code == 200
    data = response.get_json()
    assert data["activities"][0]["_id"] is not None
