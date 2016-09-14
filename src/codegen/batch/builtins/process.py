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
set {0}.exec.__c=0
set {0}.exec.__f={0}.exec
goto {0}.exec_
:{0}.exec
set %~1=0
set _proc="%~4"
:: handle infinite arguments
:{0}exec__rearg
if "%~5" neq "" (
  set _args=!_args! "%~5"
  shift
  goto :{0}exec__rearg
)
if not defined _args (start /min cmd /c "!_proc!") else (start /min cmd /c "!_proc!!_args!")
goto :eof
:{0}.exec_

set {0}.execSync={0}.execSync
set {0}.execSync.__c=0
set {0}.execSync.__f={0}.execSync
goto {0}.execSync_
:{0}.execSync
set _return_var=%~1
set _proc="%~4"
:: handle infinite arguments
:{0}execSync__rearg
if "%~5" neq "" (
  set _args=!_args! "%~5"
  shift
  goto :{0}execSync__rearg
)
if not defined _args (2>nul !_proc!) else (2>nul !_proc!!_args!)
set !_return_var!=!errorlevel!
goto :eof
:{0}.execSync_

set {0}.exit={0}.exit
set {0}.exit.__c=0
set {0}.exit.__f={0}.exit
goto {0}.exit_
:{0}.exit
if not "%4"=="" (set {0}.exitCode=%4)
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

set {0}.sleep={0}.sleep
set {0}.sleep.__c=0
set {0}.sleep.__f={0}.sleep
goto {0}.sleep_
:{0}.sleep
choice /T %~4 /C X /D X /N >nul
goto :eof
:{0}.sleep_

set {0}.exitCode=0
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
        var.name = '__process'
        bat.emit(INIT.format(var.name), 'init')
        bat.emit(CODE.format(var.name), 'decl')
        bat.decl_var('process', 'variable', global_scope=True).name = var.name
