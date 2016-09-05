@echo off
setlocal enabledelayedexpansion

set fac=fac
set ass=ass
set main=main

rem THIS FUNCTION WILL BE REMOVED IN THE FUTURE, console.log WILL REPLACE IT
set print=print
goto __after_print
:print
setlocal
set ret=%1
set str=
:__print_next
if "%2" equ "" (goto :__print_done)
set "str=%str%%2 "
shift
goto :__print_next
:__print_done
if "%str%" neq "" (echo %str%)
endlocal & (set %ret%=0)
exit /b
:__after_print


goto :__after_fac
:fac
setlocal
if %2 leq 1 (set /a __1=1) else (set /a __1=0)
if !__1! neq 0 (
set "__2=1"
) else (
set /a "__3=%2-1"
call :!fac! __4 !__3!
set /a "__5=%2*!__4!"
set "__2=!__5!"
)
endlocal & (
set /a %1=%__2%
)
exit /b
:__after_fac
goto :__after_ass
:ass
setlocal
set /a "__6=%4*1"
set /a "aa=!__6!"
set /a "__7=!aa!+1"
call set "__8=%%%3[!__7!]%%"
call set "__9=%%%2[!__8!]%%"
call set "__10=%%!__9![1]%%"
endlocal & (
set %1=%__10%
)
exit /b
:__after_ass
goto :__after_main
:main
setlocal
set "__11=__11"
set "__11[0]=1"
set "__11[1]=2"
set "__11[2]=3"
set  "x=!__11!"
set "__12=__12"
set "__12[0]=bosse"
set "__12[1]=anita"
set  "c=!__12!"
set "__13=__13"
set "__13[0]=a"
set "__13[1]=b"
set "__13[2]=!c!"
set  "y=!__13!"
call :!ass! __14 !y! !x! 0
call :!print! __15 !__14!
endlocal & (set %1=0)
exit /b
:__after_main
call :!main! __16 

