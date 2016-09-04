@echo off
setlocal enabledelayedexpansion
:main
setlocal
set /p _1=watap?
set  a=!_1!
if !a! equ snabel (
echo wow elite!
) else (
echo very noob
)
endlocal
exit /b