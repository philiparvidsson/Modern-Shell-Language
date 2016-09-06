@echo off
setlocal enabledelayedexpansion

set len=len

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


goto :__after_len
:len
setlocal
set  "b=%2"
call set "__1=%%!b![__length__]%%"
call :!print! __2 !__1!
call set "__3=%%!b![__length__]%%"
endlocal & (
set %1=%__3%
)
exit /b
:__after_len
set "__4=__4"
set "__4[0]=a"
set "__5=__5"
set "__5[0]=x"
set "__6=__6"
set "__6[0]=anita"
set "__6[1]=bosse"
set "__6[2]=carl"
set "__6[__length__]=3"
set "__5[1]=!__6!"
set "__5[2]=z"
set "__5[__length__]=3"
set "__4[1]=!__5!"
set "__4[2]=c"
set "__4[__length__]=3"
set  "a=!__4!"
call set "__7=%%!a![1]%%"
call set "__8=%%!__7![1]%%"
call set "__9=%%!a![1]%%"
call set "__10=%%!__9![1]%%"
set  "!__8![1]=dashit"
call :!len! __11 !a!
call :!print! __12 length of a is !__11!
call set "__13=%%!a![0]%%"
call :!print! __14 first element of is !__13!
call set "__15=%%!a![1]%%"
call set "__16=%%!__15![1]%%"
call set "__17=%%!__16![1]%%"
call :!print! __18 second element of second element of second element of a is !__17!

