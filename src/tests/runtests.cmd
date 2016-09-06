echo off
for %%i in (*.bat) do (echo RUNNING TEST & echo name: %%i & echo. & %%i)
echo hej
del *.bat