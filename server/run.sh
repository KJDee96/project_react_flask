#!/usr/bin/env bash

mkdir -p logs
source venv/bin/activate
gunicorn -c python:config.gunicorn "api.app:create_app()"