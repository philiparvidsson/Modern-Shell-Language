from codegen.batch.batchgen import Batch

from lexing.lexer  import Lexer
from lexing.source import StringSource
from lexing.token  import Token

from parsing.parser import Parser

import os

if __name__ == '__main__':
    functionfiles = [f for f in os.listdir('.\\tests') if os.path.splitext(f)[1] == ".func"]
    globalfunctions = ""
    for file in functionfiles:
        with open('.\\tests\\' + file, 'r') as sourcefile:
            globalfunctions += "\n" + sourcefile.read() + "\n"

    testfiles = [f for f in os.listdir('.\\tests') if os.path.splitext(f)[1] == ".test"]
    for file in testfiles:
        with open('.\\tests\\' + file, 'r') as sourcefile:
            source=StringSource(globalfunctions + sourcefile.read())

        lexer  = Lexer(source)
        parser = Parser(lexer)

        ast = parser.generate_ast()
        batch = Batch(ast)
        code = batch.generate_code()
        
        fname = os.path.splitext(file)[0]
        f = open('.\\tests\\' + fname + '.bat', 'w')
        f.write(code)
        f.close()

    # use runtests.cmd to exec all tests
    f = open('.\\tests\\runtests.cmd', 'w')
    f.write("""
@echo off
setlocal enableDelayedExpansion

set arg1=%~1
set verbose=0
if /i "%arg1:~0,1%"=="v" (set verbose=1)

for %%i in (*.bat) do (
  echo exit /b>>%%i
  if %verbose% gtr 0 (
    set str=%%i
    echo test: !str:~0,-4!
  )
  call %%i %verbose%
)

del *.bat 2>nul
echo @echo off>cleanup.cmd
echo del *.cmd 2^>nul 1^>nul>>cleanup.cmd
start cmd /D /C "cd /d "%cd%" & cleanup.cmd"
""")
    f.close()