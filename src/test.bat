@echo off
setlocal enabledelayedexpansion

set main=main

rem THIS FUNCTION WILL BE REMOVED IN THE FUTURE, console.log WILL REPLACE IT
set print=print
goto __after_print
:print
setlocal
set ret=%1
set str=
:__print_next
if "%2" equ "" (goto :__print_done)
set "str=%str%%2 "
shift
goto :__print_next
:__print_done
if "%str%" neq "" (echo %str%)
endlocal & (set %ret%=0)
exit /b
:__after_print


goto :__after_main
:main
setlocal
call :!print! __1 16 2 3
endlocal & (set %1=0)
exit /b
:__after_main
call :!main! __2 

