@ECHO OFF
REM Author Dominik Jochinger dominik.jochinger@gmx
REM script to convert all images into textfiles 1 .. 15

for /L %%i IN (0 1 9) do for /L %%j IN (1 1 15) do convert raw%%i_%%j.png -resize 4x6 -contrast-stretch 2%x99% -colorspace GRAY scaled%%i_%%j.txt