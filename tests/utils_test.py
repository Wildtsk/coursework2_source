import pytest

from app import app

params = {"poster_name": "poster_name",
          "poster_avatar": "poster_avatar",
          "pic": "pic",
          "content": "content",
          "views_count": "views_count",
          "likes_count": "likes_count",
          "pk": "pk"}

key = ("poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk")


def test_app_read_posts():
    response = app.test_client().get('/api/posts', query_string=params)
    print(response.json)
    assert response.status_code == 200
    for k in key:
        assert k in params.keys()


def test_app_read_post_by_id():
    response = app.test_client().get('api/post/<int:id>/', query_string=params)
    print(response.json)
    assert response.status_code == 200
    for k in key:
        assert k in params.keys()


def test_app_read_post_by_user_name():
    response = app.test_client().get('/api/post/<user_name>/', query_string=params)
    print(response.json)
    assert response.status_code == 200
    for k in params:
        assert k in key
