import pytest

from app import app


def test_app_read_posts():
    params = {"s": "python"}
    response = app.test_client().get('/api/posts', query_string=params)
    print(response.json)
    assert response.status_code == 200
    assert len(response.json) == 8


def test_app_read_post_by_id():
    params = {"id": 1, "s": "python"}
    response = app.test_client().get('api/post/<int:id>/', query_string=params)
    print(response.json)
    assert response.status_code == 200


def test_app_read_post_by_user_name():
    params = {"id": 1, "user_name": "Molly"}
    response = app.test_client().get('/api/post/<user_name>/', query_string=params)
    print(response.json)
    assert response.status_code == 200
    assert len(response.json) == 21