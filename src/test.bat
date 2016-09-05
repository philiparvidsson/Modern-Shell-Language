@echo off
setlocal enabledelayedexpansion
set _1=_1
set  x=_3
set  y=_1
set _3=_3
call :!y! _4 !x!
goto :eof
:_1
setlocal
call :!x! _2
echo !_2!
endlocal & (set %1=0)
exit /b

goto :eof
:_3
setlocal
endlocal & (
set %1=SNABEL LOL
)
exit /b
