@echo off
echo Downloading python packages...

pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo All packages downloaded.
) else (
    echo Error occured, try it again or contact creator.
)

pause