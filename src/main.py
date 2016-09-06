from codegen.batch import Batch

from lexing.lexer  import Lexer
from lexing.source import StringSource
from lexing.token  import Token

from parsing.parser import Parser

from parsing.draw_ast import draw_ast_tree

if __name__ == '__main__':
    source = StringSource(
"""
function show_fruit_info(f) {
    console.log('the', f.name, 'is', f.taste)
}

fruit = [] // Array declarations can be used as objects!
fruit.name = 'apple'
fruit.taste = 'sweet'

// Objects can have functions!
fruit.eat = function (s) { console.log('wow, what a', s, 'apple') }
fruit.eat('crunchy')
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
