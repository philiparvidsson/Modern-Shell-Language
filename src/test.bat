@echo off
setlocal enabledelayedexpansion
set /a a=1
set /a b=100
set /a c=1
:lbl1
if !a! leq !b! (set /a _1=1) else (set /a _1=0)
if !_1! neq 0 (
echo !a! !b! !c!
set /a _2=!a!*2
set /a a=!_2!
set /a _3=!b!+10
set /a b=!_3!
set /a _4=!c!+1
set /a c=!_4!
goto :lbl1
)