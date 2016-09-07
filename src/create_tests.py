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
    f.write("""
@echo off
setlocal enableDelayedExpansion

set arg1=%~1
set verbose=0
if /i "%arg1:~0,1%"=="v" (set verbose=1)

echo RUNNING TESTS
echo -------------
for %%i in (*.bat) do (
  echo exit /b>>%%i
  if %verbose% gtr 0 (
    set str=%%i
    echo test: %str:~0,-4%
  )
  call %%i %verbose%
)

del *.bat
echo @echo off>cleanup.cmd
echo del *.cmd 2^>nul 1^>nul>>cleanup.cmd
start cmd /D /C "cd %cd% & cleanup.cmd"
""")
    f.close()