@ECHO OFF

call %~d0%~p0\env\Scripts\activate

cd %~d0%~p0

set FLASK_DEBUG=1

set FLASK_APP=Project

set FLASK_ENV=development

flask run