"""
vps-auto-grading-software
author: venisprajapati
file-name: app.py
"""

__author__ = 'Venis Prajapati'
__license__ = 'Apache-2.0 License'
__version__ = 'v 2.0'


# This file contains code of executing main function i.e. app.py file and some file handling logic

import os
import webbrowser
from waitress import serve
from threading import Timer
from werkzeug.utils import secure_filename
from flask import Flask, render_template, redirect, send_file, request, send_from_directory
# from services.final_result_ import MakeFinalResults


students_file_name_ = 'students.jpg'

app = Flask(__name__)
UPLOAD_FOLDER_1 = './uploads'
app.config['UPLOAD_FOLDER_1'] = UPLOAD_FOLDER_1

ANSWERS = './uploads'
app.config['ANSWERS'] = ANSWERS

RESULT_FOLDER = './result'
app.config['RESULT_FOLDER'] = RESULT_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        directory = './result'
        for f in os.listdir(directory):
            os.remove(os.path.join(directory, f))

        file_students = request.files['students']
        if file_students:
            global students_file_name_
            students_file_name_ = secure_filename(file_students.filename)
            file_students.save(os.path.join(
                app.config['RESULT_FOLDER'], "students.jpg"))

        file_answers = request.files['answers']
        if file_answers:
            file_answers.save(os.path.join(
                app.config['ANSWERS'], "answers.jpg"))

        return redirect('/result')

    elif request.method == "GET":
        return render_template('index.html')

    else:
        return "Error 404: Page Not Found"


@app.route('/result', methods=['GET', 'POST'])
def result():

    if request.method == 'POST':
        return 1000000000

    elif request.method == "GET":
        return render_template('result.html')

    else:
        return "Error 404: Page Not Found"


@app.route('/info', methods=['GET'])
def info():

    return render_template('info.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


def open_web_browser():
    webbrowser.open_new('http://127.0.0.1:2102/')


# main function :- program execution will starts from here
if __name__ == '__main__':

    print("Venis Prajapati's Auto grading Software Started At PORT: http://127.0.0.1:2102/")

    Timer(1, open_web_browser).start()
    serve(app, host="127.0.0.1", port=2102)

    # app.run(port=2102, debug=True)
