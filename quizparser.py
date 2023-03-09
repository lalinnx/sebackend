from lexer import Lexer
from parser_ import Parser


class quizparser:
    def __init__(self):

        self.lexer1 = Lexer(
            "G-1,Q-1A,what is dog?,rand[/cat/dog=/you/me]Q-1B,what is cat?,rand[/you/cat/dog=/tiger]end,G-2,Q-2A,meal with?,norand[/dog=/cat/you/tiger]Q-2B,illegel to eat cat?,rand[/no/yes=]end")
        self.parser = Parser(self.lexer1.generate_tokens())
        self.tree = self.parser.parse()

    def Do_parser(self):
        for g in self.tree:
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
