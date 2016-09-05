from codegen.batch import Batch

from lexing.lexer  import Lexer
from lexing.source import StringSource
from lexing.token  import Token

from parsing.parser import Parser

from parsing.draw_ast import draw_ast_tree

if __name__ == '__main__':
    source = StringSource(
"""

function fac(x) {
    return (x <= 1) ? 1
                    : x*fac(x-1)
}

function ass(a, b, n) {
aa=n*1 // needs cast.. =(
return (a[b[aa+1]])[1]
}

function main() {
    //fn = x => x+1
    x = [1,2,3]
    c = ['bosse', 'anita']
    y = ['a', 'b', c]
    print(ass(y, x, 0))
}

main()
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
