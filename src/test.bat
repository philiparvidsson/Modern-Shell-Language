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
goto __after_exit
:__5[exit]
set "errorlevel=%~2"
goto :eof
:__after_exit

set ass=ass
set __11=__11

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
goto :__after_ass
:ass
setlocal
call set "__8=%%!__2![log]%%"
call :%~2 __9 2
call :!__8! __10 "!__9!"
endlocal & (set %1=0)
exit /b
:__after_ass
goto :__after___11
:__11
setlocal
set /a "__12=%~2*4"
endlocal & (
set /a %1=%__12%
)
exit /b
:__after___11
call :!ass! __13 "__11"

