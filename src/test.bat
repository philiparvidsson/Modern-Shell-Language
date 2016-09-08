@echo off
setlocal enabledelayedexpansion

set apa=apa

goto :__after_apa
:apa
setlocal
endlocal & (
set /a %1=1
)
exit /b
:__after_apa

