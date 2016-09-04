@echo off
setlocal enabledelayedexpansion      
set /a a=100                         
set /a b=500                         
set /a _1=!a!/10                     
set /a _2=!_1!*3                     
set /a _3=!_2!+6                     
set /a _4=!a!*3                      
set /a _5=!_4!+!_3!                  
set /a _6=2*!b!                      
set /a _7=!_6!+!_5!                  
set /a _8=1+!_7!                     
set /a c=!_8!                        
echo.!c!                             