@echo off
setlocal enabledelayedexpansion

set lewl=lewl

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


goto :__after_lewl
:lewl
setlocal
set /a "__1=%2*1"
set /a "a=!__1!"
set /a "__2=%3*1"
set /a "b=!__2!"
set /a "__3=1*%2"
set /a "__4=1*%3"
set /a "__5=!__3!+!__4!"
set "__6=heylo!__5!"
endlocal & (
set %1=%__6%
)
exit /b
:__after_lewl
set "__7=__7"
set "__7[__length__]=0"
set  "a=!__7!"
set  "!a![lol]=!lewl!"
call set "__8=%%!a![lol]%%"
call :!__8! __9 5 9
call :!print! __10 !__9!

