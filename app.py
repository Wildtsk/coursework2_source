import logging

from flask import Flask, send_from_directory, request, jsonify

from utils import get_posts_by_user
from views import main_blueprint, mane_page

# POST_PATH = "data/data.json"
# UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


app.register_blueprint(main_blueprint)

# logging.basicConfig(filename="basic.log", level=logging.INFO)


@app.route("/")
def get_posts_user():
    s = request.args.get("s")
    return jsonify(get_posts_by_user())


if __name__ == "__main__":
    app.run()


