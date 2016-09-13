#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

CODE = (
'''
set {0}={0}

set {0}.log={0}.log
goto {0}.log_
:{0}.log
set r=%1
set s=
:{0}_echo
if "%~3" equ "" (goto :{0}_done)
set "s=%s%%~3 "
shift
goto :{0}_echo
:{0}_done
if "%s%" neq "" (echo %s%) else (echo.)
set %r%=0
goto :eof
:{0}.log_
''')

#-------------------------------------------------
# GLOBALS
#-------------------------------------------------

var = None

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def emit_code(b):
    global var
    if not var:
        var = b.tempvar('string')
        var.name += '_console'
        b.emit(CODE.format(var.name), 'decl')
        b.decl_var('console', 'variable').name = var.name
