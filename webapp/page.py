from flask import (
    Blueprint, render_template, send_file
)
from werkzeug.exceptions import abort

RESUME_PATH = 'static/resume.pdf'


bp = Blueprint('page', __name__)


@bp.route("/")
def index():
    return render_template("homepage.html")


@bp.route('/resume')
def show_resume():
    return send_file(RESUME_PATH, attachment_filename='resume.pdf')
