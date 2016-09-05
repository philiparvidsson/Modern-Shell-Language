
setlocal enabledelayedexpansion
:main
setlocal enabledelayedexpansion
call :are_equal _1 42 42
echo !_1!
if !_1! neq 0 (
echo sant
) else (
echo falskt
)
endlocal
exit /b
:are_equal
setlocal
if %2 equ %3 (set /a _2=1) else (set /a _2=0)
endlocal & (
set %1=!_2!
)
exit /b
endlocal
exit /b