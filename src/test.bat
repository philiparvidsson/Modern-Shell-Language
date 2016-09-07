@echo off
setlocal enabledelayedexpansion

set assert=assert

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
if "%s%" neq "" (echo %s%)
endlocal & (set %r%=1)
exit /b
:__2_console.log_


set __5_process=__5_process

set __5_process.exit=__5_process.exit
goto __5_process.exit_
:__5_process.exit
goto :eof
:__5_process.exit_

set __5_process.exitCode=0


goto :__after_assert
:assert
setlocal
if %~3 neq %~2 (set /a __1=1) else (set /a __1=0)
if !__1! neq 0 (
call set "__3=%%!__2_console!.log%%"
call :!__3! __4 "assertion^ failed^:" "%~4"
call set "__6=%%!__5_process!.exit%%"
call :!__6! __7 1
)
endlocal & (
set /a %1=1
)
exit /b
:__after_assert
set "__8=__8"
set "__8.0=ass"
set "__8.1=2"
set "__8.2=3"
set "__8.length=3"
set  "a=!__8!"
call set "__9=%%!__2_console!.log%%"
call set "__10=%%!a!.0%%"
call :!__9! __11 "!__10!"
call :!assert! __12 1 0 "ass^^!^#^"^""

