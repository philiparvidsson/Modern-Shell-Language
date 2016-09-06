@echo off
setlocal enabledelayedexpansion

set fac=fac

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
set "__2=1"
) else (
set /a "__3=%2-1"
call :!fac! __4 !__3!
set /a "__5=%2*!__4!"
set "__2=!__5!"
)
endlocal & (
set /a %1=%__2%
)
exit /b
:__after_fac
call :!fac! __6 3
call :!print! __7 !__6!

