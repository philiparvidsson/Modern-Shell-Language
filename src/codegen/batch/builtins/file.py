#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

CODE = (
'''
set {0}={0}

set {0}.delete={0}.delete
goto {0}.delete_
:{0}.delete
setlocal
if exist "%~2" (
    del "%~2"
    set r=1
) else (
    set r=0
)
endlocal & (set %~1=%r%)
exit /b
:{0}.delete_

set {0}.exists={0}.exists
goto {0}.exists_
:{0}.exists
setlocal
if exist "%~2" (set r=1) else (set r=0)
endlocal & (set %~1=%r%)
exit /b
:{0}.exists_

set {0}.read={0}.read
goto {0}.read_
:{0}.read
setlocal
set lf=^


set "r="
for /f "delims=" %%s in (%~2) do (set "r=!r!%%s!lf!")
endlocal & (set %1=%r%)
exit /b
:{0}.read_
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
        var.name += '_file'
        p.emit(CODE.format(var.name), 'decl')

    p.scope.decl_var('file', 'variable').name = var.name
