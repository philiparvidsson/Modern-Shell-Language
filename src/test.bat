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
set /a "__2=3&%2"
endlocal & (
set /a %1=%__2%
)
exit /b
:__1_skip
set  filter=__1
set /a y=1
:lbl1
set /a "__3=!y!+1"
set /a y=!__3!
if !y! lss 10 (set /a __4=1) else (set /a __4=0)
if !__4! neq 0 (
call :!filter! __5 !y!
if !__5! neq 0 (
set /a z=!y!
echo !z!
)
goto :lbl1
)
endlocal & (set %1=0)
exit /b
:main_skip
call :!main! __6 

