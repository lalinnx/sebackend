from lexer import Lexer
from parser_ import Parser

lexer = Lexer("G{type1}[Q{question1.1,what is dog?},rand[C{choice1}C{choice2}=C{choice3}C{choice4}]Q{question1.2,what is cat?},rand[C{choice1}{choice2}C{choice3}=C{choice4}]G{type2}[Q{question2.1, what is game?},norand[C{choice1}=C{choice2}C{choice3}C{choice4}]Q{question3, what is what?},rand[C{choice1}C{choice2}=C{choice3}C{choice4}]")
parser = Parser(lexer.generate_tokens())
tree = parser.parse()
print(list(tree))

