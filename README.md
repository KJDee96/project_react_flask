# Project using Flask backend + React Frontend

## Setup dependencies
Create virtual env and activate

`python3 -m venv venv`

`source venv/bin/activate`
***
Install wheel also

`pip install wheel`
***
Install requirements

`pip install -r requirements.txt`

## Run
`gunicorn -c python:config.gunicorn "api.app:create_app()"`