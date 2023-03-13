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

    def parse(self):
        result = []
        while self.current_token is not None:
            print('parse current token:', self.current_token)
            if self.current_token.type == TokenType.CHAR:
                if self.current_token.value == "G":
                    self.advance()
                    result.append(self.parseGroup())
                elif self.current_token.value == "Q":
                    self.advance()
                    result.append(self.parseQuestion())
                    if self.current_token is None:
                        break
                    else:
                        self.checktype(TokenType.COMMA)
            else:
                self.raise_error()

        return result

    def parseGroup(self):
        print('group current token:', self.current_token)
        self.checktype(TokenType.HYPHEN)
        name = self.parseName()
        print('group current token:', name)
        self.checktype(TokenType.COMMA)

        question = []
        while self.current_token is not None:
            if self.current_token.value == "Q":
                print('group current token:', self.current_token)
                self.advance()
                question.append(self.parseQuestion())
            elif self.current_token is None:
                break
            else:
                x = self.parseName()
                if x == "end":
                    if self.current_token is None:
                        break
                    if self.current_token.type == TokenType.COMMA:
                        self.checktype(TokenType.COMMA)
                        break
        print('end group')

        return Group(name, question)

    def parseQuestion(self):
        self.checktype(TokenType.HYPHEN)
        name = self.parseName()
        print('current token:', name)
        self.checktype(TokenType.COMMA)
        ques = self.parseName()
        print('current token:', ques)
        print('question current token:', self.current_token)
        # self.checktype(TokenType.CHAR)
        choice = self.parseChoice()

        return Question(name, ques, choice)

    def parseChoice(self):
        ans = ''
        print('choice current token:', self.current_token)
        self.checktype(TokenType.LEFTSQUARE)
        print('current token:', self.current_token)
        choice = []

        while self.current_token is not TokenType.RIGHTSQUARE:
            self.checktype(TokenType.ASTERISK)
            self.checktype(TokenType.ASTERISK)
            current_choice = self.parseName()
            choice.append(current_choice)
            print('current token:', current_choice)
            if self.current_token.type == TokenType.ANSWER:
                ans = current_choice
                self.advance()

            if self.current_token.type == TokenType.RIGHTSQUARE:
                self.advance()
                break
            print('current token::', self.current_token)

        print('end choice current token::', self.current_token)

        return Choice(choice, ans)

    def parseName(self):
        text = str(self.current_token.value)
        self.advance()
        while self.current_token is not None and self.current_token.type in (TokenType.CHAR, TokenType.NUMBER):
            text += str(self.current_token.value)
            self.advance()
        return text
