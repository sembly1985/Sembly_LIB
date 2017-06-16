@echo off

setlocal EnableDelayedExpansion

set Lowercase=a b c d e f g h i j k l m n o p q r s t u v w x y z
set Capital=A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

set var=%1
for %%a in (%var%) do call :replace %%a

mkdir %1
cd %1
mkdir config
mkdir Doc
mkdir Dev
mkdir PublicInt
mkdir Source
cd ..
copy module_c.template .\%1\Source\%var%.c
copy module_h.template .\%1\PublicInt\%var%.h
copy module_c.template .\%1\config\%var%_config.c
copy module_h.template .\%1\config\%var%_config.h
copy module_c.template .\%1\Dev\%var%_unittest.c
copy module_h.template .\%1\Dev\%var%_unittest.h

:replace
set "n="
set "word2="
set word=%1
:loop
set /a n+=1
set one=!word:~-%n%,1!
if %one% leq Z if %one% geq a (
  if "!Lowercase:%one%=%one%!" equ "%Lowercase%" (
    call :C %one% & goto next
  ) else (call :L %one% & goto next)
)
set "word2=%one%%word2%"
:next
if "!word:~%n%!" neq "" goto loop
set var=!var:%word2%=%word2%!
goto :eof

:L
for %%a in (%Lowercase%) do if /i %1==%%a set "word2=%%a%word2%" & goto :eof

:C
for %%a in (%Capital%) do if /i %1==%%a set "word2=%%a%word2%" & goto :eof