#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

CODE = (
'''
set {0}={0}
set {0}.__c=0
set {0}.__f={0}
goto {0}_
:{0}
setlocal
set r=%1
set s=
:{0}_next
if "%~4" equ "" (goto {0}_done)
set "s=%s%%~4 "
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

def emit_code(bat):
    global var
    if not var:
        var = bat.tempvar('string')
        var.name = '__readline'
        bat.emit(CODE.format(var.name), 'decl')
        bat.decl_var('readline', 'variable', global_scope=True).name = var.name
