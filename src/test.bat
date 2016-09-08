@echo off
setlocal enabledelayedexpansion

set print_all=print_all

set __7_console=__7_console

set __7_console.log=__7_console.log
goto __7_console.log_
:__7_console.log
setlocal
set r=%1
set s=
:__7_console_echo
if "%~2" equ "" (goto :__7_console_done)
set "s=%s%%~2 "
shift
goto :__7_console_echo
:__7_console_done
if "%s%" neq "" (echo %s%) else (echo.)
endlocal & (set %r%=1)
exit /b
:__7_console.log_


goto :__after_print_all
:print_all
setlocal
set /a "i=0"
set  "s="
:lbl1
call set "__2=%%%~2.length%%"
if !i! lss !__2! (set /a __1=1) else (set /a __1=0)
if !__1! neq 0 (
call set "__3=%%%~2.!i!%%"
set "__4=!__3! and "
set "__5=!s!!__4!"
set  "s=!__5!"
set /a "__6=!i!"
set /a "i=!i!+1"
goto :lbl1
)
call set "__8=%%!__7_console!.log%%"
call :!__8! __9 "!s!"
endlocal & (set %1=0)
exit /b
:__after_print_all
set "__10=__10"
set "__10.0=one"
set "__10.1=two"
set "__10.2=three"
set "__10.length=3"
call :!print_all! __11 "!__10!"

