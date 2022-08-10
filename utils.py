from flask import json


def get_posts_all() -> list[dict]:
    """Возвращает все посты"""
    with open('data/data.json', "r", encoding="utf-8") as file:
        return json.load(file)


def get_posts_by_user(user_name: str) ->list[dict]:
    """возвращает посты определенного пользователя
    обработка ошибки при вводе цифры, обработка пустого списка"""
    result = []
    for post in get_posts_all():
        try:
            if user_name.lower() in post['poster_name'].lower():
                result.append(post)
        except AttributeError:
            return "Такого имени у нас нет"
    if len(result) > 0:
        return result
    else:
        return "Совпадений не найдено"


def get_comments_all() -> list[dict]:
    """Возвращает все комментарии"""
    with open("data/comments.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_comments_by_post_id(comments_id) -> list[dict]:
    """возвращает комментарии определенного поста"""
    result = []
    try:
        comments_id = int(comments_id)
        for comments in get_comments_all():
            if comments_id == comments['post_id']:
                result.append(comments)
        return result
    except ValueError:
        return "Введите правильный номер поста"


def search_for_posts(query: str) -> list[dict]:
    """возвращает список постов по ключевому слову"""
    result = []
    for post in get_posts_all():
        if query.lower() in post['content'].lower():
            result.append(post)
    if len(result) > 0:
        return result
    else:
        return "418"


def get_post_by_pk(pk: str) -> dict:
    """возвращает один пост по его идентификатору. """
    try:
        post_id = int(pk)
        for post in get_posts_all():
            if post_id == post['pk']:
                return post
        else:
            return "Такого поста пока нет"
    except ValueError:
        return "Введите правильный номер поста"

