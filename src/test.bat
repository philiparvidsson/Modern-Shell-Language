@echo off
setlocal enabledelayedexpansion


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


set "__1=__1"
set "__1[0]=a"
set "__1[1]=b"
set "__1[2]=c"
set  "a=!__1!"
set /a "i=1"
call set "__2=%%!a![1]%%"
set  "None=hej"
call set "__3=%%!a![!i!]%%"
call :!print! __4 a[ !i! ] is  !__3!

