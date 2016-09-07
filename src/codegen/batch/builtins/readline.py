#-------------------------------------------------
# GLOBALS
#-------------------------------------------------

var = None

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def emit_code(parser):
    if not var:
        var = parser.tempvar('string')
        code = (
'''
set readline=readline
goto __after_readline
:readline
setlocal
set ret=%1
set str=
:__readline_next
if "%2" equ "" (goto :__readline_done)
set "str=%str%%2 "
shift
goto :__readline_next
:__readline_done
set /p tmp=%str%
endlocal & (set %ret%=%tmp%)
exit /b
:__after_readline
'''.format(var.name))
        parser.emit(code, 'decl')

    parser.scope.declare_variable('readline', 'variable').name = var.name
