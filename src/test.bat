@echo off
setlocal enabledelayedexpansion


set __3=__3
set __3[log]=__3[log]
goto __after_print
:__3[log]
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


set /a "a=0"
:lbl1
set /a "__1=!a!"
set /a "a=!a!+1"
if !__1! lss 10 (set /a __2=1) else (set /a __2=0)
if !__2! neq 0 (
call set "__4=%%!__3![log]%%"
call :!__4! __5 !a!
goto :lbl1
)

