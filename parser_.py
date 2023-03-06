from tokens import TokenType
from node import Choice, Question, Group


class Parser:

    def __init__(self, tokens):
        self.current_token = None
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self):
        raise Exception("Invalid syntax")

    def checktype(self, T):
        if self.current_token is not None and self.current_token.type == T:
            self.advance()

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        while self.current_token is not None:
            if self.current_token.type == TokenType.CHAR:
                if self.current_token.value == "G":
                    return self.parseGroup()
                elif self.current_token.value == "Q":
                    return self.parseQuestion()
            else:
                self.raise_error()

    def parseGroup(self):
        self.checktype(TokenType.LEFTCURLY)
        name = self.parseName()
        self.checktype(TokenType.LEFTSQUARE)
        self.advance()

        question = []
        i = 0

        while self.current_token is not None:
            if self.current_token.value == "Q":
                question[i] = self.parseQuestion()
                i += 1
                self.advance()
            if self.current_token.type == TokenType.RIGHTAQUARE: break

        return Group(name, question)

    def parseQuestion(self):
        self.checktype(TokenType.LEFTCURLY)
        name = self.parseName()
        self.checktype(TokenType.CHAR)
        ques = self.parseName
        self.checktype(TokenType.QUESTION)
        self.checktype(TokenType.RIGHTCURLY)
        self.checktype(TokenType.COMMA)
        self.checktype(TokenType.CHAR)
        random = False
        if self.current_token.value == "rand":
            random = True
        elif self.current_token.value == "norand":
            random = False
        else:
            self.raise_error()
        choice = self.parseChoice()

        return Question(name, ques, random, choice)

    def parseChoice(self):
        ans = ''
        self.checktype(TokenType.LEFTSQUARE)
        self.advance()
        choice = []
        i = 0
        while True:
            self.checktype(TokenType.LEFTCURLY)
            choice[i] = self.parseName()
            if self.checktype(TokenType.ANSWER):
                ans = choice[i]
            i += 1
            self.advance()
            if self.current_token.type == TokenType.RIGHTAQUARE: break

        return Choice(choice, ans)

    def parseName(self):
        text = self.current_token.value
        self.advance()
        while self.current_token is not None and self.current_token.type in (TokenType.CHAR, TokenType.NUMBER):
            text += self.current_token.value
            self.advance()
        return text
