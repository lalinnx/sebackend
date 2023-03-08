from lexer import Lexer
from parser_ import Parser

lexer1 = Lexer("G-1,Q-1A,what is dog?,rand[/cat/dog=/you/me]Q-1B,what is cat?,rand[/you/cat/dog=/tiger]end,G-2,Q-2A,meal with?,norand[/dog=/cat/you/tiger]Q-2B,illegel to eat cat?,rand[/no/yes=]end")
parser = Parser(lexer1.generate_tokens())
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

