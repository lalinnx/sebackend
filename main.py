import node
from lexer import Lexer
from parser_ import Parser
from QuizObject import *
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

lexer1 = Lexer(
    "G-1,Q-1A,what is dog?,rand[/cat/dog=/you/me]Q-1B,what is cat?,rand[/you/cat/dog=/tiger]end,G-2,Q-2A,meal with?,norand[/dog=/cat/you/tiger]Q-2B,illegel to eat cat?,rand[/no/yes=]end")
lexer2 = Lexer(
    "G-1,P-1.5,Q-1A,หมาคือ++-*/%""''$#@!?.{}()_<>=^&|:;\อะไร?,rand[**แมว**หมา=**จิ้งจก**เธอ]Q-1B,แมวคืออะไร?,rand[**เธอ**แมว**หมา=**เสือhiuggu]end,Q-2,P-0.5,เม่นคืออะไร?,rand[**เธอ**แมว**หมา=**เสือ],Q-3,P-2,คนคืออะไร?,rand[**เธอ**แมว**หมา=**เสือ],G-2,P-2,Q-2A,หมาคืออะไร?,rand[**แมว**หมา=**จิ้งจก**เธอ]")
parser = Parser(lexer2.generate_tokens())
tree = parser.parse()

group_id = 0
prepared_quizGroup = QuizGroupObject()
prepared_quizQuestion = QuizQuestionObject()

def questionMethod(q, group_id):
    print(q.name)
    print(q.ques)
    print("Point:", q.point)

    ch = q.choice.choice



for g in tree:
    if type(g) is node.Group:
        group_id += 1


        print("=====================")
        print("Group:", g.name)
        print("------------------")
        qlist = g.Question

        for q in qlist:
            questionMethod(q, group_id)
    else:
        print("********no group*********")
        questionMethod(g, 0)

print()
for i in prepared_quizGroup.getQuizGroup():
    print(i)
for i in prepared_quizQuestion.getQuizQuestion():
    print(i)

