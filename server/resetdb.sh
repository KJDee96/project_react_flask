#!/usr/bin/env bash

# Drop and create database
sudo -u postgres dropdb project_test
sudo -u postgres createdb project_test

# Run migrations
flask db upgrade

# switch user to postgres, open psql and redirect sql file to db (LOCAL SYSTEM SETUP)
sudo -u postgres psql -d project_test -q < /home/kieran/project_test_localhost-2020_07_24_05_50_00-dump.sql