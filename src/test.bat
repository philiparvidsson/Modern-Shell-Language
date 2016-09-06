@echo off
setlocal enabledelayedexpansion

set show_fruit_info=show_fruit_info

set __1=__1
set __1[log]=__1[log]
goto __after_print
:__1[log]
setlocal
set ret=%1
set str=
:__print_next
if "%~2" equ "" (goto :__print_done)
set "str=%str%%~2 "
shift
goto :__print_next
:__print_done
if "%str%" neq "" (echo %str%)
endlocal & (set %ret%=0)
exit /b
:__after_print

set __7=__7

goto :__after_show_fruit_info
:show_fruit_info
setlocal
call set "__2=%%!__1![log]%%"
call set "__3=%%%~2[name]%%"
call set "__4=%%%~2[taste]%%"
call :!__2! __5 "the" "!__3!" "is" "!__4!"
endlocal & (set %1=0)
exit /b
:__after_show_fruit_info
set "__6=__6"
set "__6[__length__]=0"
set  "fruit=!__6!"
set  "!fruit![name]=apple"
set  "!fruit![taste]=sweet"
goto :__after___7
:__7
setlocal
call set "__8=%%!__1![log]%%"
call :!__8! __9 "wow, what a" "%~2" "apple"
endlocal & (set %1=0)
exit /b
:__after___7
set  "!fruit![eat]=__7"
call set "__10=%%!fruit![eat]%%"
call :!__10! __11 "crunchy"

