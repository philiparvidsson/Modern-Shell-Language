@echo off
setlocal enabledelayedexpansion

set main=main
set __1=__1

goto :main_skip
:main
setlocal
goto :__1_skip
:__1
setlocal
set /a __2=%2/2
set /a __3=!__2!*2
if !__3! equ %2 (set /a __4=1) else (set /a __4=0)
endlocal & (
set /a %1=%__4%
)
exit /b
:__1_skip
set  filter=__1
set /a y=1
:lbl1
set /a __5=!y!+1
set /a y=!__5!
if !y! lss 10 (set /a __6=1) else (set /a __6=0)
if !__6! neq 0 (
call :!filter! __7 !y!
set  z=!__7!
call :!filter! __8 !y!
if !__8! neq 0 (
set /a a=!y!
set  b=!z!
echo !a!
)
goto :lbl1
)
endlocal & (set %1=0)
exit /b
:main_skip
call :!main! __9 

