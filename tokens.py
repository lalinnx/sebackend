from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    CHAR = 0
    NUMBER = 1
    COMMA = 2
    ASTERISK = 3
    ANSWER = 4
    LEFTSQUARE = 5
    RIGHTSQUARE = 6
    HYPHEN = 7


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")
