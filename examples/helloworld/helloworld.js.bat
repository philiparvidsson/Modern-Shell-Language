@echo off
setlocal enabledelayedexpansion


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


set __4=__4
goto __4_
:__4
setlocal
set r=%1
set s=
:__4_next
if "%2" equ "" (goto __4_done)
set "s=%s%%2 "
shift
goto __4_next
:__4_done
set /p t=%s%
endlocal & (set %r%=%t%)
exit /b
:__4_


call set "__2=%%!__1_console!.log%%"
call :!__2! __3 "hello world^^!"
call :!__4! __5 
set  "day=!__5!"
call set "__6=%%!__1_console!.log%%"
call :!__6! __7 "it^'s nice that it^'s" "!day!"

