@echo off
setlocal enabledelayedexpansion

set assert=assert

set __2=__2
set __2[log]=__2[log]
goto __after_print
:__2[log]
setlocal
set ret=%1
set str=
:__print_next
if "%~2" equ "" (goto :__print_done)
set "str=%str%%~2 "
shift
goto :__print_next
:__print_done
if "%str%" neq "" (echo %str%)
endlocal & (set %ret%=0)
exit /b
:__after_print


set __5=__5

set __5[exit]=__5[exit]
goto __5[exit]_
:__5[exit]
goto :eof
:__5[exit]_

set __5[exitCode]=5


goto :__after_assert
:assert
setlocal
if %~3 neq %~2 (set /a __1=1) else (set /a __1=0)
if !__1! neq 0 (
call set "__3=%%!__2![log]%%"
call :!__3! __4 "assertion failed:" "%~4"
call set "__6=%%!__5![exit]%%"
call :!__6! __7 1
)
endlocal & (
set /a %1=1
)
exit /b
:__after_assert
call set "__8=%%!__2![log]%%"
call set "__9=%%!__5![exitCode]%%"
call :!__8! __10 "!__9!"
call :!assert! __11 1 1 "ass"

