from codegen.batch.batchgen import Batch

from lexing.lexer  import Lexer
from lexing.source import StringSource
from lexing.token  import Token

from parsing.parser import Parser

from parsing.draw_ast import draw_ast_tree

if __name__ == '__main__':
    source = StringSource(
"""
function foo() { console.log('foo'); return false }
function bar() { console.log('bar'); return true }

a = false

/* Regular if-then-else statements */
if (a) foo() else bar() // Braces can be omitted for single statements.

if (a) {
    foo()
}
else {
    bar()
}


/* Ternary operator */
fn = a ? foo : bar
fn()

/* Short-circuiting */
foo() && bar() // Only prints 'foo' since foo() returns false!
foo() || bar() // Prints 'foo' and 'bar'
""")
    lexer  = Lexer(source)
    parser = Parser(lexer)

    ast = parser.generate_ast()
    draw_ast_tree(ast)

    batch = Batch(ast)
    code = batch.generate_code()

    f = open('test.bat', 'w')
    f.write(code)
    f.close()
    print
    print
    print code
