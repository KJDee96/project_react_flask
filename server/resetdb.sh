#!/usr/bin/env bash

# Drop and create database
sudo -u postgres dropdb project
sudo -u postgres createdb project

# Run migrations
flask db upgrade

# switch user to postgres, open psql and redirect sql file to db (LOCAL SYSTEM SETUP)
# sudo -u postgres psql -d project_test -q < /home/kieran/project-dump.sql