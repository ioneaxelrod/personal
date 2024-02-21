from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('page', __name__)


@bp.route("/")
def index():
    return render_template("homepage.html")


@app.route('/resume')
def show_resume():
    with open(RESUME_PATH, READ_BYTES) as static_file:
        return send_file(static_file, attachment_filename='resume.pdf')
