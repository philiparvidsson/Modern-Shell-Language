@echo off
setlocal enabledelayedexpansion
set _1=_1
set  y=_1
set /a x=5
call :!y! _2 !x!
goto :eof
:_1
setlocal
echo %2
endlocal & (set %1=0)
exit /b
