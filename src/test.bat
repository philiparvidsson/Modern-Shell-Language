@echo off
setlocal enabledelayedexpansion

set foo=foo

set __1_console=__1_console

set __1_console.log=__1_console.log
goto __1_console.log_
:__1_console.log
setlocal
set r=%1
set s=
:__1_console_echo
if "%~2" equ "" (goto :__1_console_done)
set "s=%s%%~2 "
shift
goto :__1_console_echo
:__1_console_done
if "%s%" neq "" (echo %s%) else (echo.)
endlocal & (set %r%=1)
exit /b
:__1_console.log_

set bar=bar

goto :__after_foo
:foo
setlocal
call set "__2=%%!__1_console!.log%%"
call :!__2! __3 "foo"
endlocal & (
set /a %1=0
)
exit /b
:__after_foo
goto :__after_bar
:bar
setlocal
call set "__4=%%!__1_console!.log%%"
call :!__4! __5 "bar"
endlocal & (
set /a %1=1
)
exit /b
:__after_bar
set /a "a=0"
if !a! neq 0 (
call :!foo! __6 
) else (
call :!bar! __7 
)
if !a! neq 0 (
call :!foo! __8 
) else (
call :!bar! __9 
)
if !a! neq 0 (
set "__10=!foo!"
) else (
set "__10=!bar!"
)
set  "fn=!__10!"
call :!fn! __11 
call :!foo! __12 
if !__12! neq 0 (
call :!bar! __13 
)
call :!foo! __15 
set /a __14=0
if !__15! neq 0 (
set /a __14=1
) else (
call :!bar! __16 
if !__16! neq 0 (
set /a __14=1
)
)

