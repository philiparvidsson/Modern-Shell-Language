from codegen.batch import Batch

from lexing.lexer  import Lexer
from lexing.source import StringSource
from lexing.token  import Token

from parsing.parser import Parser

from parsing.draw_ast import draw_ast_tree

if __name__ == '__main__':
    source = StringSource(
"""

function len(a) {
b=a
print(b['__length__'])
    return b['__length__']
}

a = ['a', ['x', ['anita', 'bosse', 'carl'], 'z'], 'c']

((a[1])[1])[1] = 'dashit'

print('length of a is', len(a))
print('first element of is', a[0])
print('second element of second element of second element of a is', ((a[1])[1])[1])
}



""")
    lexer  = Lexer(source)
    parser = Parser(lexer)

    ast = parser.generate_abstract_syntax_tree()
    draw_ast_tree(ast)

    batch = Batch(ast)
    code = batch.generate_code()

    f = open('test.bat', 'w')
    f.write(code)
    f.close()
    print
    print
    print code
