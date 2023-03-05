from tokens import TokenType

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
                if self.current_token == "G":
                    result = self.parseGroup()
                elif self.current_token == "Q": 
                    result = self.parseQuestion()
            else: self.raise_error()

        return result

    def parseGroup(self):
        self.checktype("LEFTCURLY")
        name = self.parseName()
        self.current_token.type in("RIGHTCURLY")
        self.checktype("LEFTSQUARE")
        self.advance

        question = []
        i = 0  

        while True:
            self.current_token == "Q"
            question[i] = self.parseQuestion()
            i+=1
            self.advance
            if self.current_token.type in ("RIGHTAQUARE"): break
        return question
        
    def parseQuestion(self):
        self.checktype("LEFTCURLY")
        name = self.parseName()
        self.current_token.type in("COMMA")
        self.checktype("CHAR")
        Question = self.current_token
        self.checktype("QUESTION")
        self.checktype("RIGHTCURLY")
        self.checktype("COMMA")
        self.checktype("CHAR")
        if self.current_token == "rand":
            random = True
        elif self.current_token == "norand":
            random = False
        else: self.raise_error()
        choice = self.parseChoice()

        return name+Question+random+choice
    
    def parseChoice(self):
        self.checktype("LEFTSQUARE")
        self.advance
        choice = []
        i = 0     
        while True:
            self.current_token == "C"
            self.checktype("LEFTCURLY")
            choice[i] = self.parseName() 
            self.current_token.type in("RIGHTCURLY")
            if self.checktype("ANSWER"):
                ans = choice[i]
            i+=1
            self.advance
            if self.current_token.type in ("RIGHTAQUARE"): break

        return choice+ans

    def parseName(self):
        str = self.current_token
        self.advance()
        while self.current_token.type in ("CHAR" | "NUMBER"):        
            str+=self.current_token
            self.advance()
        return str