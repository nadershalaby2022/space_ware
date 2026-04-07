@echo off
cd /d "%~dp0"
echo =====================================
echo Plane Battle - Controls
echo Arrow Keys = Move
echo Space      = Fire missile
echo =====================================
python -m streamlit run app.py
pause
