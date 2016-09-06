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
endlocal & (
call set "__1=%%!b![__length__]%%"
set %1=!__1!
)
exit /b
:__after_len
set "__2=__2"
set "__2[0]=a"
set "__3=__3"
set "__3[0]=x"
set "__4=__4"
set "__4[0]=anita"
set "__4[1]=bosse"
set "__4[2]=carl"
set "__4[__length__]=3"
set "__3[1]=!__4!"
set "__3[2]=z"
set "__3[__length__]=3"
set "__2[1]=!__3!"
set "__2[2]=c"
set "__2[__length__]=3"
set  "a=!__2!"
call :!len! __5 !a!
call :!print! __6 !__5!

