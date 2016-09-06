from codegen.batch import Batch

from lexing.lexer  import Lexer
from lexing.source import StringSource
from lexing.token  import Token

from parsing.parser import Parser

import os

if __name__ == '__main__':
    files = [f for f in os.listdir('.\\tests') if os.path.splitext(f)[1] == ".test"]
    for file in files:
        with open('.\\tests\\' + file, 'r') as sourcefile:
            source=StringSource(sourcefile.read())

        lexer  = Lexer(source)
        parser = Parser(lexer)

        ast = parser.generate_abstract_syntax_tree()
        batch = Batch(ast)
        code = batch.generate_code()
        
        fname = os.path.splitext(file)[0]
        ff = open('.\\tests\\' + fname + '.bat', 'w')
        ff.write(code)
        ff.close()

    # use runtests.cmd to exec all tests
    f = open('.\\tests\\runtests.cmd', 'w')
    f.write('@echo off')
    f.write('\nfor %%i in (*.bat) do (echo RUNNING TEST & echo name: %%i & echo. & %%i)')
    f.write('\ndel *.bat')
    f.close()