@echo off
setlocal enabledelayedexpansion

set main=main

goto :main_skip
:main
setlocal
set /a a=2
set /a "__1=2<<!a!"
set /a a=!__1!
echo !a!
endlocal & (set %1=0)
exit /b
:main_skip
call :!main! __2 

