#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

CODE = (
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
''')

#-------------------------------------------------
# GLOBALS
#-------------------------------------------------

var = None

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def emit_code(p):
    global var
    if not var:
        var = p.tempvar('string')
        p.emit(CODE.format(var.name), 'decl')

    p.scope.decl_var('readline', 'variable').name = var.name
