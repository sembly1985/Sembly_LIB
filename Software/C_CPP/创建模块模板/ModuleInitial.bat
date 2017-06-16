@echo off

setlocal EnableDelayedExpansion

copy TextReplacing.py .\%1\config\TextReplacing.py
copy TextReplacing.py .\%1\Dev\TextReplacing.py
copy TextReplacing.py .\%1\PublicInt\TextReplacing.py
copy TextReplacing.py .\%1\Source\TextReplacing.py

set param_0=%0
set param_1=%1
set param_2=%2
set param_3=%3

shift /0
shift /0
shift /0
shift /0
if %param_3%==3 (set var="%0")
if %param_3%==4 (set var="%0 %1")
if %param_3%==5 (set var="%0 %1 %2")
if %param_3%==6 (set var="%0 %1 %2 %3")
if %param_3%==7 (set var="%0 %1 %2 %3 %4")
if %param_3%==8 (set var="%0 %1 %2 %3 %4 %5")
if %param_3%==9 (set var="%0 %1 %2 %3 %4 %5 %6")
if %param_3%==10 (set var="%0 %1 %2 %3 %4 %5 %6 %7")
if %param_3%==11 (set var="%0 %1 %2 %3 %4 %5 %6 %7 %8")
if %param_3%==12 (set var="%0 %1 %2 %3 %4 %5 %6 %7 %8 %9")

cd %param_1%\config
python TextReplacing.py %param_1% %param_2% config %var%
del /q /s TextReplacing.py
cd..

cd Dev
python TextReplacing.py %param_1% %param_2% Dev %var%
del /q /s TextReplacing.py
cd..

cd PublicInt
python TextReplacing.py %param_1% %param_2% PublicInt %var%
del /q /s TextReplacing.py
cd..

cd Source
python TextReplacing.py %param_1% %param_2% Source %var%
del /q /s TextReplacing.py
cd..

cd..