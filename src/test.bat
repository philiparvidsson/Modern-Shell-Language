@echo off
setlocal enabledelayedexpansion


set __2_console=__2_console

set __2_console.log=__2_console.log
goto __2_console.log_
:__2_console.log
setlocal
set r=%1
set s=
:__2_console_echo
if "%~2" equ "" (goto :__2_console_done)
set "s=%s%%~2 "
shift
goto :__2_console_echo
:__2_console_done
if "%s%" neq "" (echo %s%) else (echo.)
endlocal & (set %r%=1)
exit /b
:__2_console.log_


set /a "i=0"
:lbl1
if !i! lss 10 (set /a __1=1) else (set /a __1=0)
if !__1! equ 0 (goto :lbl1_)
call set "__3=%%!__2_console!.log%%"
call :!__3! __4 !i!
set /a "__5=!i!"
set /a "i=!i!+1"
goto :lbl1
:lbl1_
)

