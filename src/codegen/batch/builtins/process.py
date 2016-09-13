#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

INIT = (
'''
set {0}={0}

set {0}.argv={0}.argv
set {0}.argv.length=0

:{0}_argv
if "%~1" neq "" (
    set "{0}.argv.!{0}.argv.length!=%~1"
    set /a {0}.argv.length+=1
    shift
    goto {0}_argv
)
''')

CODE = (
'''
set {0}.exec={0}.exec
goto {0}.exec_
:{0}.exec
set _proc="%~3"
set _args="%~4"
if !_args! == "" (start /min cmd /c "!_proc!") else (start /min cmd /c "!_proc! !_args!")
set %~1=0
goto :eof
:{0}.exec_

set {0}.execSync={0}.execSync
goto {0}.execSync_
:{0}.execSync
set _proc="%~3"
set _args="%~4"
if !_args! == "" (start /wait /min "!_proc!") else (start /wait /min "!_proc! !_args!")
set %~1=!errorlevel!
goto :eof
:{0}.execSync_

set {0}.exit={0}.exit
goto {0}.exit_
:{0}.exit
if not "%3"=="" (set {0}.exitCode=%3)
:{0}_unwind_stack
set x=%0
set x=!x:~0,1!
if "!x!"==":" (
    (goto) 2>nul & (
        set {0}.exitCode=%{0}.exitCode%
        goto :{0}_unwind_stack
    )
) else (
    exit /b !{0}.exitCode!
)
goto :eof
:{0}.exit_

set {0}.exitCode=0
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
        var.name += '_process'
        p.emit(INIT.format(var.name), 'init')
        p.emit(CODE.format(var.name), 'decl')

    p.scope.decl_var('process', 'variable').name = var.name
