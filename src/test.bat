@echo off
setlocal enabledelayedexpansion

set main=main

goto :__after_main
:main
setlocal
set /a a=10
set /a b=2
set /a c=16
endlocal & (set %1=0)
exit /b
:__after_main
call :!main! __1 

