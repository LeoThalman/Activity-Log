import pytest
from flask import Flask, url_for
import sys
sys.path.append('..')
import app
import requests

URL = 'http://localhost:5001'



def test_activity_errors_on_invalid_id():
    post_url = URL + "/api/activities/aaaaaaaaaaaaaaaaaaaaaaaa"
    response = requests.get(post_url)
    assert response.status_code == 404
