from lexer import Lexer
from parser_ import Parser
from QuizObject import *
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

lexer1 = Lexer(
    "G-1,Q-1A,what is dog?,rand[/cat/dog=/you/me]Q-1B,what is cat?,rand[/you/cat/dog=/tiger]end,G-2,Q-2A,meal with?,norand[/dog=/cat/you/tiger]Q-2B,illegel to eat cat?,rand[/no/yes=]end")
lexer2 = Lexer(
    "G-name1,Q-1,หมาคืออะไร?,rand[**แมว**หมา=**จิ้งจก**เธอ]Q-2,แมวคืออะไร?,rand[**เธอ**แมว**หมา=**เสือ]end")
parser = Parser(lexer2.generate_tokens())
tree = parser.parse()

group_id = 0
prepared_quizGroup = QuizGroupObject()
prepared_quizQuestion = QuizQuestionObject()

print()
print()
for g in tree:
    group_id += 1
    prepared_answer = Answer()

    print("=====================")
    print("Group:", g.name)
    print("------------------")
    qlist = g.Question

    prepared_quizGroup.addQuizGroup(
        groupName=g.name,
        pickCount=len(g.Question),
        questionPoints=1,
        assessmentID=1,
    )

    for q in qlist:

        print(q.name)
        print(q.ques)
        print("rand: ", q.ran)
        ch = q.choice.choice
        for i in ch:
            if i == q.choice.Ans:
                print("answer choice: ", i)
                prepared_answer.addAnswer(answer_text=i,answer_weight=100)
            else:
                print("choice: ", i)
                prepared_answer.addAnswer(answer_text=i,answer_weight=0)
        print("------------------")

    prepared_quizQuestion.addQuizQuestion(
        question_name="Question"+str(group_id),
        question_text=q.name,
        quiz_group_id=group_id,
        question_type="multiple_choice_question",
        position=1,
        points_possible=1,
        correct_comments="",
        incorrect_comments="",
        neutral_comments="",
        text_after_answers="",
        answers=[]
    )

print()
for i in prepared_quizGroup.getQuizGroup():
    print(i)
for i in prepared_quizQuestion.getQuizQuestion():
    print(i)

