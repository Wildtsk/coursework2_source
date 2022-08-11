import pytest

from app import app


def test_get_posts_by_user():
    params = {"poster_name": "leo"}
    response = app.test_client().get("/post/", query_string=params)
    print(response.json)
    assert response.status_code == 200
