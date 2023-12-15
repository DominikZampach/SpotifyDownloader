@echo off
echo Downloading python packages...

if exist myenv (
    echo Virtual env already exists, going to download packages only.
) else (
    echo Creating virtual env (can take little longer)...
    python -m venv myenv
)

call myenv\Scripts\activate

pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo All packages downloaded, you can leave this script.
) else (
    echo Error occured, try it again or contact creator.
)

pause