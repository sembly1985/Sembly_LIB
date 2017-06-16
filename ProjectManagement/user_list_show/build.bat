pyinstaller -F user_list_show.py
copy /Y .\dist\user_list_show.exe .\
rd /S /Q __pycache__
rd /S /Q build
rd /S /Q dist
del /S /Q *.spec