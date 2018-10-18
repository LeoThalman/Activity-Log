import os
import tempfile
import pytest
import sys
sys.path.append('..')
from app import app

@pytest.fixture
def setup_module(app):
    app.setup_tests()

@pytest.fixture
def client():
    app.config["SERVER_NAME"] = "test.local"
    client = app.test_client()

    # Pushing the app context allows us to make calls to the app like url_for
    # as if we were the running Flask app. Makes testing routes more resiliant.
    ctx = app.app_context()
    ctx.push()

    yield client

    ctx.pop()
