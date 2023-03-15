from ParseQuiz import parse_quiz
import json
from datetime import datetime
from ReadDocx import readDoc
from flask import Flask, make_response, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import json_util

ALLOWED_EXTENSIONS = ('docx')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
client = MongoClient(
    'mongodb+srv://work21123:0881496697_Zaa@lmsquizimporter.897habv.mongodb.net/?retryWrites=true&w=majority')
db = client['lmsquiz']
CORS(app)


def no_page(error):
    return "<h1>no route to try to access</h1>"


def wrong_params(error):
    return "<h1> wrong param in document check your file's extension</h1>"


@app.route('/')
def hello():
    return {"message": "index page"}, 201


@app.route('/api/allQuiz/')
def all_Quiz():
    allquiz = []
    quizdataTable = db['quizdata']
    for data in quizdataTable.find():
        allquiz.append(data)
    return app.response_class(
        response=json_util.dumps(allquiz),
        status=200,
        mimetype='application/json'
    )


@app.route('/api/Quiz/<user_name>')
def UserWithID(user_name):
    userQuizzes = []
    quizdataTable = db['quizdata']
    for data in quizdataTable.find({"author": user_name}):
        userQuizzes.append(data)
    return app.response_class(
        response=json_util.dumps(userQuizzes),
        status=200,
        mimetype='application/json'
    )


@app.route('/api/upload', methods=['POST'])
def upload_file():

    try:
        quizdataTable = db['quizdata']
        file = request.files['files']
        author = request.form['author'].replace(" ", "_")
        title = request.form['title']
        createdate = datetime.today().replace(microsecond=0)
        status = "ready to import"
        fileType = file.filename.split(".")[1]
        if (fileType not in ALLOWED_EXTENSIONS):
            return 'bad request!', 400
        quiz_text = readDoc(file=file, fileType=fileType).getText()
        quizgroup = parse_quiz(quiz_text=quiz_text)
        quizdataTable.insert_one({'author': author, 'title': title,
                                 'createDate': createdate, 'qData': quizgroup, 'status': status})
        itm = quizdataTable.find_one({'author': author, 'title': title,
                                 'createDate': createdate, 'qData': quizgroup, 'status': status})
    except Exception as e:
        return f"Couldn't upload file {e}"

    return make_response(jsonify({'deviloperID':str(itm.get('_id')) ,'author': author, 'title': title, 'createDate': createdate, 'status': status, 'qData': quizgroup}),200)


app.register_error_handler(404, no_page)
app.register_error_handler(400, no_page)
