from tokens import TokenType
from node import Choice,Question,Group

class Parser:
    def __init__(self, tokens) :
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self):
        raise Exception("Invalid syntax")

    def checktype(self,T):
        if self.current_token.type in (T):
            self.advance

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
   
    def parse(self):
        while self.current_token != None:
            if self.current_token.type in (TokenType.CHAR):
                if self.current_token.value == "G":
                    result = self.parseGroup()
                elif self.current_token.value == "Q": 
                    result = self.parseQuestion()
            else: self.raise_error()

        return result

    def parseGroup(self):
        self.checktype(TokenType.LEFTCURLY)
        name = self.parseName()
        self.current_token.type in(TokenType.RIGHTCURLY)
        self.checktype(TokenType.LEFTSQUARE)
        self.advance

        question = []
        i = 0  

        while True:
            if self.current_token.value == "Q":
                question[i] = self.parseQuestion()
                i+=1
                self.advance
            else: self.raise_error()
            if self.current_token.type in (TokenType.RIGHTAQUARE): break

        return Group(name,question)
        
    def parseQuestion(self):
        self.checktype(TokenType.LEFTCURLY)
        name = self.parseName()
        self.current_token.type in(TokenType.COMMA)
        self.checktype(TokenType.CHAR)
        ques = self.parseName
        self.checktype(TokenType.QUESTION)
        self.checktype(TokenType.RIGHTCURLY)
        self.checktype(TokenType.COMMA)
        self.checktype(TokenType.CHAR)
        if self.current_token.value == "rand":
            random = True
        elif self.current_token.value == "norand":
            random = False
        else: self.raise_error()
        choice = self.parseChoice()

        return Question(name,ques,random,choice)
    
    def parseChoice(self):
        self.checktype(TokenType.LEFTSQUARE)
        self.advance
        choice = []
        i = 0     
        while True:
            self.current_token.value == "C"
            self.checktype(TokenType.LEFTCURLY)
            choice[i] = self.parseName() 
            self.current_token.type in(TokenType.RIGHTCURLY)
            if self.checktype(TokenType.ANSWER):
                ans = choice[i]
            i+=1
            self.advance
            if self.current_token.type in (TokenType.RIGHTAQUARE): break

        return Choice(choice,ans)

    def parseName(self):
        str = self.current_token
        self.advance()
        while self.current_token.type in (TokenType.CHAR | TokenType.NUMBER):        
            str+=self.current_token
            self.advance()
        return str
