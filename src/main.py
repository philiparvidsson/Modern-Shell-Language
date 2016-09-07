from codegen.batch.batchgen import Batch

from lexing.lexer  import Lexer
from lexing.source import StringSource
from lexing.token  import Token

from parsing.parser import Parser

from parsing.draw_ast import draw_ast_tree

if __name__ == '__main__':
    source = StringSource(
"""
function assert(a, b, s) {
    if (a != b) {
        console.log('assertion failed:', s)
        process.exit(1)
    }

    return true
}

//assert(false, true, 'ass')

function ass(a) {
console.log(a(2))
}

ass(function (q) { return q*4 })
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
