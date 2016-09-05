@echo off
setlocal enabledelayedexpansion

set fac=fac
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


goto :__after_fac
:fac
setlocal
if %2 leq 1 (set /a __1=1) else (set /a __1=0)
if !__1! neq 0 (
endlocal & (
set /a %1=1
)
exit /b
)
set /a "__2=%2-1"
call :!fac! __3 !__2!
set /a "__4=%2*!__3!"
endlocal & (
set /a %1=%__4%
)
exit /b
:__after_fac
goto :__after_main
:main
setlocal
set /a b=0
if !b! neq 0 (
set "__5=noob"
) else (
set "__5=not oob"
)
set  x=!__5!
call :!print! __6 !b! !x!
endlocal & (set %1=0)
exit /b
:__after_main
call :!main! __7 

