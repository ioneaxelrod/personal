from flask import Flask, render_template, send_file
app = Flask(__name__)

RESUME_PATH = '/path/of/file.pdf'
READ_BYTES = 'rb'


@app.route('/')
def hello_world():
    return render_template("homepage.html")


@app.route('/resume')
def get_resume():
    with open(RESUME_PATH, READ_BYTES) as static_file:
        return send_file(static_file, attachment_filename='resume.pdf')
