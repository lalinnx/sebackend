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
    point: float()

    def __init__(self, n, q, c, p):
        self.name = n
        self.ques = q
        self.choice = c
        self.point = p

    # def __repr__(self):
    #     return self.name + self.ques + self.ran + str(self.choice)


class Group:
    name: any
    Question: list
    point: float()
    def __init__(self, n, q, p):
        self.name = n
        self.Question = q
        self.point=p

    # def __repr__(self):
    #     rep = str(self.name) + ',' + str(self.Question) + ')'
    #     return rep
