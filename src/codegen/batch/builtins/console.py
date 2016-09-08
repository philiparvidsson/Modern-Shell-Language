#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

CODE = (
'''
set {0}={0}

set {0}.log={0}.log
goto {0}.log_
:{0}.log
setlocal
set r=%1
set s=
:{0}_echo
if "%~2" equ "" (goto :{0}_done)
set "s=%s%%~2 "
shift
goto :{0}_echo
:{0}_done
if "%s%" neq "" (echo %s%) else (echo.)
endlocal & (set %r%=1)
exit /b
:{0}.log_
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
        var.name += '_console'
        p.emit(CODE.format(var.name), 'decl')

    p.scope.decl_var('console', 'variable').name = var.name
