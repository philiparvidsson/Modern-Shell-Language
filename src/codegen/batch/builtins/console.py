#-------------------------------------------------
# GLOBALS
#-------------------------------------------------

var = None

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def emit_code(parser):
    global var
    if not var:
        var = parser.tempvar('string')
        code = (
'''
set {0}={0}
set {0}[log]={0}[log]
goto __after_print
:{0}[log]
setlocal
set ret=%1
set str=
:__print_next
if "%~2" equ "" (goto :__print_done)
set "str=%str%%~2 "
shift
goto :__print_next
:__print_done
if "%str%" neq "" (echo %str%)
endlocal & (set %ret%=0)
exit /b
:__after_print
'''.format(var.name))
        parser.emit(code, 'decl')

    parser.scope.declare_variable('console', 'variable').name = var.name
