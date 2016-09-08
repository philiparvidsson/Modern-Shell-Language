#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

CODE = (
'''
set {0}={0}
goto {0}_
:{0}
setlocal
set r=%1
set s=
:{0}_next
if "%2" equ "" (goto {0}_done)
set "s=%s%%2 "
shift
goto {0}_next
:{0}_done
set /p t=%s%
endlocal & (set %r%=%t%)
exit /b
:{0}_
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
