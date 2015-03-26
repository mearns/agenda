
@ECHO OFF

start console -w "GIT AGENDA" -d "%~dp0"
start console -w "DEMO AGENDA" -d "%~dp0\demo"
start console -w "TEST AGENDA" -d "%~dp0\demo"

start cmd /c cd "%~dp0" ^&^& start gvim -p -c ":simalt ~x"

if "%PYTHON_HOME%"=="" GOTO NO_HH
    start hh "%PYTHON_HOME%.\Doc\python275.chm"
:NO_HH

