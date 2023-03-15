from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    CHAR = 0
    NUMBER = 1
    ASTERISK = 2
    ANSWER = 3
    LEFTSQUARE = 4
    RIGHTSQUARE = 5
    HYPHEN = 6


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")
