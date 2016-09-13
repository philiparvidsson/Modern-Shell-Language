#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

CODE = (
'''
set {0}={0}

set {0}.delete={0}.delete
goto {0}.delete_
:{0}.delete
if exist "%~3" (
    del "%~3"
    set r=1
) else (
    set r=0
)
set %~1=%r%
goto :eof
:{0}.delete_

set {0}.exists={0}.exists
goto {0}.exists_
:{0}.exists
if exist "%~3" (set r=1) else (set r=0)
set %~1=%r%
goto :eof
:{0}.exists_

set {0}.read={0}.read
goto {0}.read_
:{0}.read
set lf=^


set "r="
for /f "delims=" %%s in (%~3) do (set "r=!r!%%s!lf!")
set %1=%r%
goto :eof
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
