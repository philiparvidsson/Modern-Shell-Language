from codegen.batch import Batch

from lexing.lexer  import Lexer
from lexing.source import StringSource
from lexing.token  import Token

from parsing.parser import Parser

from parsing.draw_ast import draw_ast_tree

if __name__ == '__main__':
    source = StringSource(
"""

a = 1
b = 100
c = 1
while (a <= b) {
    print(a, b, c)
    a *= 2
    b += 10
    c++
}

""")
    lexer  = Lexer(source)
    parser = Parser(lexer)

    ast = parser.generate_abstract_syntax_tree()
    draw_ast_tree(ast)

    batch = Batch(ast)
    code = batch.generate_code()
    print
    print
    print code
