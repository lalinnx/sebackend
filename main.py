from lexer import Lexer
from parser_ import Parser

lexer = Lexer("G{type1}[Q{question1.1,what is dog?},rand[C{choice1}C{choice2}=ans]")
parser = Parser(lexer.generate_tokens())
tree = parser.parse()
print(list(tree))

