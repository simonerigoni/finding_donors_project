rem Run launch ps1 script named as this cmd script
@echo off
set scriptName=%~n0
set scriptDir=%~dp0
powershell -NoProfile -ExecutionPolicy Bypass -File "%scriptDir%%scriptName%.ps1"
