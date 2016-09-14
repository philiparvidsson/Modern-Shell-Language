#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

CODE = (
'''
set {0}={0}

set {0}.delete={0}.delete
set {0}.delete.__c=0
set {0}.delete.__f={0}.delete
goto {0}.delete_
:{0}.delete
if exist "%~4" (
    del "%~4
    set r=1
) else (
    set r=0
)
set %~1=%r%
goto :eof
:{0}.delete_

set {0}.exists={0}.exists
set {0}.exists.__c=0
set {0}.exists.__f={0}.exists
goto {0}.exists_
:{0}.exists
if exist "%~4" (set r=1) else (set r=0)
set %~1=%r%
goto :eof
:{0}.exists_

set {0}.read={0}.read
set {0}.read.__c=0
set {0}.read.__f={0}.read
goto {0}.read_
:{0}.read
set lf=^


set "r="
for /f "delims=" %%s in (%~4) do (set "r=!r!%%s!lf!")
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

def emit_code(bat):
    global var
    if not var:
        var = bat.tempvar('string')
        var.name = '__file'
        bat.emit(CODE.format(var.name), 'decl')
        bat.decl_var('file', 'variable', global_scope=True).name = var.name
