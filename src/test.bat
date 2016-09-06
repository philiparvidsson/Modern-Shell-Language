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
set "__1[0]=1"
set "__1[1]=b"
set "__1[2]=c"
set "__1[__length__]=3"
set  "a=!__1!"
set /a "i=1"
set /a "i=0"
:lbl1
set /a "__2=!i!"
set /a "i=!i!+1"
call set "__4=%%!a![__length__]%%"
if !__2! lss !__4! (set /a __3=1) else (set /a __3=0)
if !__3! neq 0 (
call set "__5=%%!a![!i!]%%"
call :!print! __6 a[ !i! ] is  !__5!
goto :lbl1
)

