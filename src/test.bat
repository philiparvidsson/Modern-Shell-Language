@echo off
setlocal enabledelayedexpansion

set a=a
set __1=__1

rem ----------------------------------------------
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
rem ----------------------------------------------


goto :__after_a
:a
setlocal
goto :__after___1
:__1
setlocal
set "__2=%2%2"
set "__3=hej!__2!"
call :!print! __4 !__3!
endlocal & (set %1=0)
exit /b
:__after___1
endlocal & (
set %1=__1
)
exit /b
:__after_a
call :!a! __5 
set  "c=!__5!"
call :!c! __6 
call :!a! __7 qq
call :!__7! __8 lol

