from lexer import Lexer
from parser_ import Parser
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

lexer1 = Lexer("G-1,Q-1A,what is dog?,rand[/cat/dog=/you/me]Q-1B,what is cat?,rand[/you/cat/dog=/tiger]end,G-2,Q-2A,meal with?,norand[/dog=/cat/you/tiger]Q-2B,illegel to eat cat?,rand[/no/yes=]end")
lexer2 = Lexer("G-1,Q-1A,หมาคืออะไร?,rand[**แมว**หมา=**จิ้งจก**เธอ]Q-1B,แมวคืออะไร?,rand[**เธอ**แมว**หมา=**เสือ]end")
parser = Parser(lexer2.generate_tokens())
tree = parser.parse()

print()
print()
for g in tree:
    print("=====================")
    print("Group:", g.name)
    print("------------------")
    qlist = g.Question
    for q in qlist:
        print(q.name)
        print(q.ques)
        print("rand: ", q.ran)
        ch = q.choice.choice
        for i in ch:
            if i == q.choice.Ans:
                print("answer choice: ", i)
            else:
                print("choice: ", i)
        print("------------------")

