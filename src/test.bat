@echo off
setlocal enabledelayedexpansion

set __2=__2

set "__1=__1"
set "__1[__length__]=0"
set  "a=!__1!"
set  "!a![q]=ass"
goto :__after___2
:__2
setlocal
call set "__3=%%!this![q]%%"
endlocal & (
set %1=%__3%
)
exit /b
:__after___2
set  "!a![lol]=__2"
call set "__4=%%!a![lol]%%"
call :!__4! __5 

