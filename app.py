import logging

from flask import Flask, send_from_directory
from views import main_blueprint, mane_page

# POST_PATH = "data/data.json"
# UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


app.register_blueprint(main_blueprint)

# logging.basicConfig(filename="basic.log", level=logging.INFO)


@app.route("/")
def static_dir():
    return mane_page()


app.run()


