# terminal project

terminal is an exercise in Django

The project has only one app:
* flights 

for populate the Flight model table with demo flights:
python manage.py loaddata  flights.json

for running the project:
pycharm run --> edit configuration:
script: D:\save\terminal\manage.py
script parameters: runserver 0.0.0.0:8000

open url: http://127.0.0.1:8000/flights/


