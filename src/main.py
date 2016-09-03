from lexing.lexer  import Lexer
from lexing.source import StringSource
from lexing.token  import Token

from parsing.parser import Parser

from parsing.draw_ast import draw_ast_tree

if __name__ == '__main__':
    source = StringSource(
"""
x="bosse"
asd=2
y=2*X
""")
    lexer  = Lexer(source)
    parser = Parser(lexer)

    ast = parser.generate_abstract_syntax_tree()
    draw_ast_tree(ast)
