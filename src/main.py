from lexing.lexer  import Lexer
from lexing.source import StringSource
from lexing.token  import Token

from parsing.parser import Parser

from parsing.draw_ast import draw_ast_tree

if __name__ == '__main__':
    source = StringSource(
"""
func bosse(x,y,z)
    a=1
    b=2*a
end
""")
    lexer  = Lexer(source)
    parser = Parser(lexer)

    ast = parser.generate_abstract_syntax_tree()
    draw_ast_tree(ast)
