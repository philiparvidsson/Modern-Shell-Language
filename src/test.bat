@echo off
setlocal enabledelayedexpansion

set __2=__2

set __3=__3
set __3[log]=__3[log]
goto __after_print
:__3[log]
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


set "__1=__1"
set "__1[__length__]=0"
set  "a=!__1!"
set  "!a![q]=ass"
goto :__after___2
:__2
setlocal
call set "__4=%%!__3![log]%%"
call set "__5=%%!this![q]%%"
echo !__5!
call :!__4! __6 "ass" "!__5!"
endlocal & (set %1=0)
exit /b
:__after___2
set  "!a![lol]=__2"
set this=!a![lol]
call set "__7=%%!a![lol]%%"
call :!__7! __8
