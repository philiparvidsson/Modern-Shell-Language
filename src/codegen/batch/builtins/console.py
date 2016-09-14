#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

CODE = (
'''
set {0}={0}

set {0}.log={0}.log
set {0}.log.__c=0
set {0}.log.__f={0}.log
goto {0}.log_
:{0}.log
set r=%1
set s=
:{0}_echo
if "%~4" equ "" (goto :{0}_done)
set "s=%s%%~4 "
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

def emit_code(bat):
    global var
    if not var:
        var = bat.tempvar('string')
        var.name = '__console'
        bat.emit(CODE.format(var.name), 'decl')
        bat.decl_var('console', 'variable', global_scope=True).name = var.name
