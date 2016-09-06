@echo off
setlocal enabledelayedexpansion


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


set "__1=__1"
set "__2=__2"
set "__2[0]=hej"
set "__2[__length__]=1"
set "__1[0]=!__2!"
set "__1[__length__]=1"
set  "a=!__1!"
call set "__3=%%!a![0]%%"
call set "__4=%%!a![0]%%"
set  "!__3![0]=ass"
call set "__5=%%!a![0]%%"
call set "__6=%%!__5![0]%%"
set  "b=!__6!"
call set "__7=%%!a![0]%%"
call set "__8=%%!__7![0]%%"
set  "d=!__8!"
call :!print! __9 !b! !d!

