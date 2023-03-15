import node
from lexer import Lexer
from parser_ import Parser
from QuizObject import *
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

lexer1 = Lexer(
    "G-1,Q-1A,what is dog?[/cat/dog=/you/me]Q-1B,what is cat?[/you/cat/dog=/tiger]end,G-2,Q-2A,meal with?[/dog=/cat/you/tiger]Q-2B,illegel to eat cat?[/no/yes=]end")
lexer2 = Lexer(
    "G-1*P-1*Q-1A* ข้อใดไม่ใช้ซอฟต์แวร์ประสงค์ร้าย?[*Redhat=*Virus*Trojan*Security Killer]Q-1B*Software ประสงค์ร้าย ข้อใดไม่ถูกต้อง?[*Virus,www=* Keylogger , Security killer* Spyware , Ransomware* Virus , Trojan]end,G-2* P-2*Q-2A* Malwareที่สามารถขยายตัวเพื่อกินพื้นที่บนอุปกรณ์ทําให้พื้นที่เต็มคืออะไร?[*Worms=*Virus* Security  Killer* Ransomware]Q-2B*ข้อใดต่อไปนีโดนซอฟเเวร์ประสงค์ร้ายเเบบ Spyware?[*จอยโดนเก็บข้อมูลส่วนตัวส่งไปให้เเฮกเกอร์=*จินโดนบันทึกการกดเเป้นพิม*เเจคสันคอมของเค้าโดนทําลายระบบป้องกัน*จินยองคอมของเค้าโดนไวรัส]end")
parser = Parser(lexer2.generate_tokens())
tree = parser.parse()

group_id = 0
prepared_quizGroup = QuizGroupObject()
prepared_quizQuestion = QuizQuestionObject()

def questionMethod(q, group_id):
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(q.name)
    print(q.ques)
    print("Point:", q.point)
    print("Answer:",q.choice.Ans)
    print("All Choice:",q.choice.choice)
    print("⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄")

    ch = q.choice.choice



for g in tree:
    if type(g) is node.Group:
        group_id += 1

        print("=====================")
        print("Group:", g.name,g.point)
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

