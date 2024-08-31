@echo off

call C:\Users\LENOVO\Desktop\Albin_Web\Django_Class\Scripts\activate.bat
cd C:\Users\LENOVO\Desktop\Project\MyJobPortal\jobportal
start cmd /k python manage.py runserver
timeout /t 5 /nobreak >nul
start http://127.0.0.1:8000