class Choice(object):
    choice: list
    Ans: any

    def __repr__(self):
        return self.choice + self.Ans


class Question:
    name: any
    ques: any
    ran: bool
    choice: Choice

    def __repr__(self):
        return self.name + self.ques + self.ran + self.choice


class Group:
    name: any
    Question: list

    def __repr__(self):
        return self.name + self.Question
