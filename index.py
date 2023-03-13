from QuizObject import *
from lexer import Lexer
from parser_ import Parser
import json
from datetime import datetime
from readDoc import readDoc
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import json_util

ALLOWED_EXTENSIONS = ('doc', 'docx')


app = Flask(__name__)
client = MongoClient(
    'mongodb+srv://work21123:0881496697_Zaa@lmsquizimporter.897habv.mongodb.net/?retryWrites=true&w=majority')
db = client['lmsquiz']
CORS(app)


def no_page(error):
    return "<h1>no route to try to access</h1>"


def wrong_params(error):
    return "<h1> wrong param in document check your file's extension</h1>"


def parse_quiz(quiz_text):

    # Tokenize the quiz text using the Lexer class
    lexer = Lexer(quiz_text)
    tokens = lexer.generate_tokens()

    # Parse the tokens using the Parser class
    parser = Parser(tokens)
    parse_tree = parser.parse()

    # Prepare the quiz group and question objects
    quiz_group = QuizGroupObject()
    quiz_question = QuizQuestionObject()
    group_id = 0

    # Loop through each group in the parse tree
    for group in parse_tree:
        group_id += 1
        question_list = group.Question

        # Add the quiz group object to the prepared_quizGroup
        quiz_group.addQuizGroup(
            groupName=group.name,
            pickCount=len(question_list),
            questionPoints=1,
            assessmentID=1
        )

        # Loop through each question in the group
        for question in question_list:
            choices = question.choice.choice
            prepared_answer = Answer()

            # Loop through each choice in the question
            for choice in choices:
                if choice == question.choice.Ans:
                    print("answer choice: ", choice)
                    prepared_answer.addAnswer(
                        answer_text=choice, answer_weight=100)
                else:
                    print("choice: ", choice)
                    prepared_answer.addAnswer(
                        answer_text=choice, answer_weight=0)

            # Add the quiz question object to the prepared_quizQuestion
            quiz_question.addQuizQuestion(
                question_name="Question"+str(group_id),
                question_text=question.name,
                quiz_group_id=group_id,
                question_type="multiple_choice_question",
                position=1,
                points_possible=1,
                correct_comments="",
                incorrect_comments="",
                neutral_comments="",
                text_after_answers="",
                answers=prepared_answer.getAnswers()
            )

    return quiz_group.getQuizGroup(), quiz_question.getQuizQuestion()


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
        category = request.form['category']
        createdate = datetime.today().replace(microsecond=0)
        status = "ready to import"
        fileType = file.filename.split(".")[1]
        if (fileType not in ALLOWED_EXTENSIONS):
            return 'bad request!', 400
        quiztext = readDoc(file=file, fileType=fileType).getText()
        quizgroup = parse_quiz(quiztext=quiztext)
        quizdataTable.insert_one({'author': author, 'category': category,
                                 'createDate': createdate, 'qData': json.dumps(quizgroup), 'status': status})

    except Exception as e:
        return f"Couldn't upload file {e}"

    # return jsonify(f"Uploading file {file.filename}")
    return jsonify(f"Uploading file {file.filename} 'author':{author},'category':{category},'createDate':{createdate},'status':{status},'qData':{quizgroup} ")



app.register_error_handler(404, no_page)
app.register_error_handler(400, no_page)
