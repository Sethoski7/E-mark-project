
"""
file-name: app.py
"""


# This file contains code of executing main function i.e. app.py file and some file handling logic

import os
import webbrowser
from waitress import serve
from threading import Timer
from werkzeug.utils import secure_filename
from flask import Flask, render_template, redirect, send_file, request, send_from_directory
from main import process_image_files

students_file_name_ = 'students.jpg'
current_directory = os.getcwd()
print("Current Directory:", current_directory)
# telling flask where to find the uploaded files in the folder
app = Flask(__name__)
UPLOAD_FOLDER_1 = r'E:\Users\HP 250\ExamChecker\exam-checker\uploads'
app.config['UPLOAD_FOLDER_1'] = UPLOAD_FOLDER_1

ANSWERS = r'E:\Users\HP 250\ExamChecker\exam-checker\uploads'
app.config['ANSWERS'] = ANSWERS

#RESULT_FOLDER = './result'
#app.config['RESULT_FOLDER'] = RESULT_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        file_students = request.files['students']
        if file_students:
            file_students_path = os.path.join(
                app.config['UPLOAD_FOLDER_1'], "students.jpg")
            file_students.save(file_students_path)
            print("Saved students file to:", file_students_path)

            

        file_answers = request.files['answers']
        if file_answers:
            file_answers_path = os.path.join(
                app.config['ANSWERS'], "answers.jpg")
            file_answers.save(file_answers_path)
            print("Saved students file to:", file_answers_path)

        # do actual calculation/marking 
        df = process_image_files('./uploads')
        pass_percentage = (df['df'].value_counts(normalize=True)['Pass']*100).round(2)# this is to give it a percentage

        return redirect('/result')
    

    elif request.method == "GET":
        return render_template('index.html')

    else:
        return "Error 404: Page Not Found"

'''
        directory = './result'
        for f in os.listdir(directory):
            os.remove(os.path.join(directory, f))

        file_students = request.files['students'] # just to match the name object in the html
        if file_students:
            global students_file_name_
            students_file_name_ = secure_filename(file_students.filename)
            file_students.save(os.path.join(
                app.config['RESULT_FOLDER'], "students.jpg")) # save the result in the result folder and name it students.jpg
'''

        


@app.route('/result', methods=['GET', 'POST'])
def result():

    
    if request.method == 'POST':
        return 1000000000

    elif request.method == "GET":
        return render_template('result.html', pass_percentage=pass_percentage, df=df)

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
