from codegen.batch.batchgen import Batch

from lexing.lexer  import Lexer
from lexing.source import StringSource
from lexing.token  import Token

from parsing.parser import Parser

from debugging.ast import visualize
from optimization.optimizer import Optimizer

if __name__ == '__main__':
    source = StringSource(
"""
for (i=0;i<10;i++) console.log(i)

""")
    lexer  = Lexer(source)
    parser = Parser(lexer)

    ast = parser.generate_ast()
    print 'before optimization'
    visualize(ast)

    optimizer = Optimizer()
    optimizer.optimize_ast(ast)

    print
    print 'after optimziation'
    visualize(ast)

    batch = Batch(ast)
    code = batch.generate_code()

    f = open('test.bat', 'w')
    f.write(code)
    f.close()
    print
    print
    print code
