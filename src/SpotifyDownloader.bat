call myenv\Scripts\activate

start cmd /c "python server.py"

start cmd /c "python main.py"

REM For testing error occuring
::start /b cmd /c "python main.py"
::IF %ERRORLEVEL% NEQ 0 (
::    echo Chyba při spouštění main.py. Stiskněte Enter pro ukončení.
::    pause
::    exit /b %ERRORLEVEL%
::)

::call \myenv\Scripts\deactivate