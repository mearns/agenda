
@ECHO OFF

start console -w "DEMO AGENDA" -d "%~dp0"
start console -w "GIT AGENDA" -d "%~dp0"

start cmd /c cd "%~dp0" ^&^& start gvim -p -c ":simalt ~x"

if "%PYTHON_HOME%"=="" GOTO NO_HH
    start hh "%PYTHON_HOME%.\Doc\python275.chm"
:NO_HH
