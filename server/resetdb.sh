#!/usr/bin/env bash

sudo -u postgres dropdb project_test
sudo -u postgres createdb project_test
flask db upgrade