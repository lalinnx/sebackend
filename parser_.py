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
        else:
            raise ValueError("Illegal argument:", self.current_token)

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    # def doIterate(self):
    #     while self.current_token is not None:

    def parse(self):
        result = []
        while self.current_token is not None:
            print('parse current token:', self.current_token)
            if self.current_token.type == TokenType.CHAR:
                if self.current_token.value == "G":
                    self.advance()
                    result.append(self.parseGroup())
                elif self.current_token.value == "Q":
                    result =  self.parseQuestion()
            else:
                self.raise_error()

        return result

    def parseGroup(self):
        print('group current token:', self.current_token)
        self.checktype(TokenType.LEFTCURLY)

        name = self.parseName()
        print('current token:', self.current_token)
        self.checktype(TokenType.RIGHTCURLY)

        question = []
        print('current token:', self.current_token)
        self.checktype(TokenType.LEFTSQUARE)
        print('current token:', self.current_token)
        while self.current_token is not None:
            if self.current_token.value == "Q":
                self.advance()
                question.append(self.parseQuestion())
            if self.current_token.value == "G": break

        print('end group current token:', self.current_token)

        return Group(name, question)

    def parseQuestion(self):
        self.checktype(TokenType.LEFTCURLY)
        name = self.parseName()
        self.checktype(TokenType.COMMA)
        self.checktype(TokenType.CHAR)
        ques = self.parseName
        self.checktype(TokenType.QUESTION)
        self.checktype(TokenType.RIGHTCURLY)
        self.checktype(TokenType.COMMA)
        print('question current token:', self.current_token)
        # self.checktype(TokenType.CHAR)
        random = False
        if self.current_token.value == "rand":
            random = True
        elif self.current_token.value == "norand":
            random = False
        else:
            self.raise_error()
        self.advance()
        choice = self.parseChoice()

        return Question(name, ques, random, choice)

    def parseChoice(self):
        ans = ''
        print('choice current token:', self.current_token)
        self.checktype(TokenType.LEFTSQUARE)
        print('current token:', self.current_token)
        self.advance()
        current_choice = 0
        choice = []

        while self.current_token is not TokenType.RIGHTSQUARE:
            print("nejfwefiuweifihfifief")
            self.checktype(TokenType.LEFTCURLY)
            print('1current token:', self.current_token)
            current_choice = self.parseName()
            choice.append(current_choice)
            self.checktype(TokenType.RIGHTCURLY)
            print('2current token:', self.current_token)
            if self.current_token.type == TokenType.RIGHTSQUARE:
                break
            if self.current_token.type == TokenType.ANSWER:
                ans = current_choice
                self.advance()
            self.advance()
            print('3current token:', self.current_token)
            if self.current_token.type == TokenType.RIGHTSQUARE:
                break

        self.checktype(TokenType.RIGHTSQUARE)
        print('end choice current token:', self.current_token)

        return Choice(choice, ans)

    def parseName(self):
        text = self.current_token.value
        self.advance()
        while self.current_token is not None and self.current_token.type in (TokenType.CHAR, TokenType.NUMBER):
            text += str(self.current_token.value)
            self.advance()
        return text
