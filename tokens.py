from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    CHAR = 0
    NUMBER = 1
    COMMA = 2
    QUESTION = 3
    ANSWER = 4
    LEFTSQUARE = 5
    RIGHTAQUARE = 6
    LEFTCURLY = 7
    RIGHTCURLY = 8

@dataclass
class Token:
    type: TokenType
    value: any = None
    
    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")