@echo off
setlocal
cd /d "%~dp0"

title CVF Workspace Setup
set "CVF_GUI_SWITCH=-Gui"
if "%CVF_GUI_SMOKE_TEST%"=="1" set "CVF_GUI_SWITCH=-GuiSmokeTest"
powershell.exe -NoProfile -ExecutionPolicy Bypass -Sta -File "%~dp0Initialize-CVF-Operator-Workspace.ps1" %CVF_GUI_SWITCH%
set "CVF_EXIT_CODE=%ERRORLEVEL%"

if not "%CVF_EXIT_CODE%"=="0" (
  echo.
  echo CVF Workspace Setup did not complete. Review the message above.
  pause
)

exit /b %CVF_EXIT_CODE%
