import os
import tempfile
import pytest
import sys
sys.path.append('..')
from app import app, setup_tests


@pytest.fixture()
def setup_module():
    setup_tests()

@pytest.fixture
def client():
    app.config["SERVER_NAME"] = "test.local"
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()

    yield client

    ctx.pop()
