class Choice(object):
    choice: list
    Ans: any

    def __init__(self, c, a):
        self.choice = c
        self.Ans = a

    # def __repr__(self):
    #     return str(self.choice), self.Ans


class Question:
    name: any
    ques: any
    choice: Choice

    def __init__(self, n, q, c):
        self.name = n
        self.ques = q
        self.choice = c

    # def __repr__(self):
    #     return self.name + self.ques + self.ran + str(self.choice)


class Group:
    name: any
    Question: list
    Point : float()

    def __init__(self, n, q, p):
        self.name = n
        self.Question = q
        self.Point = p

    # def __repr__(self):
    #     rep = str(self.name) + ',' + str(self.Question) + ')'
    #     return rep
