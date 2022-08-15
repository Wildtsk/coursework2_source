from flask import Flask, request, render_template, jsonify

from utils import get_posts_by_user, get_posts_all, get_post_by_pk
from views import main_blueprint

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(main_blueprint)


@app.route('/api/posts', methods=['GET'])
def read_posts():
    return jsonify(get_posts_all())


@app.route('/api/post/<int:post_id>/', methods=['GET'])
def read_post_by_id(post_id):
    return jsonify(get_post_by_pk(post_id))


@app.route('/api/post/<user_name>/', methods=['GET'])
def read_post_by_user_name(user_name):
    return jsonify(get_posts_by_user(user_name))


if __name__ == "__main__":
    app.run()

response = app.test_client().get('/api/posts')

print(response.status_code)
print(response.data)
