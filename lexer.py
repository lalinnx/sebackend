from tokens import Token, TokenType
import re

WHITESPACE = ' \n\t '
NUMBER = ' 0123456789 '
CHAR = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
NAMECHAR = ' ,+/%"$#@!?.{}()_<>^&|:;\ ' + "'"
thai_pattern = re.compile("[\u0E00-\u0E7F]+")


class Lexer:
    def __init__(self, text):
        self.current_char = None
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '.' or self.current_char in NUMBER:
                yield self.generate_number()
            elif self.current_char in CHAR or thai_pattern.search(self.current_char):
                yield self.generate_char()
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.ASTERISK)
            elif self.current_char == '[':
                self.advance()
                yield Token(TokenType.LEFTSQUARE)
            elif self.current_char == ']':
                self.advance()
                yield Token(TokenType.RIGHTSQUARE)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.HYPHEN)
            elif self.current_char == '=':
                self.advance()
                yield Token(TokenType.ANSWER)
            elif self.current_char in NAMECHAR:
                yield self.generate_namechar()
            else:
                raise Exception(f"Illegal character '{self.current_char}'")

    def generate_char(self):
        char_str = self.current_char.encode('utf-8').decode('utf-8')
        self.advance()

        while self.current_char is not None and (self.current_char in CHAR or thai_pattern.search(self.current_char)):
            char_str += self.current_char.encode('utf-8').decode('utf-8')
            self.advance()

        return Token(TokenType.CHAR, char_str)

    def generate_namechar(self):
        char_str = self.current_char.encode('utf-8').decode('utf-8')
        self.advance()

        while self.current_char is not None and (
                self.current_char in CHAR or self.current_char in NAMECHAR or thai_pattern.search(self.current_char)):
            char_str += self.current_char.encode('utf-8').decode('utf-8')
            self.advance()

        return Token(TokenType.CHAR, char_str)

    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()
        final_number = 0

        while self.current_char is not None and (self.current_char == '.' or self.current_char in NUMBER):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advance()
        if decimal_point_count >= 1:
            final_number = float(number_str)
        else:
            final_number = int(number_str)

        return Token(TokenType.NUMBER, final_number)
