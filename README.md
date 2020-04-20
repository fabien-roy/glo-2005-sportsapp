# SportsApp

![Build](https://github.com/ExiledNarwal28/glo-2005-sportsapp/workflows/Build/badge.svg?branch=master)
[![codecov](https://codecov.io/gh/ExiledNarwal28/glo-2005-sportsapp/branch/master/graph/badge.svg?token=R9AKC1L5PE)](https://codecov.io/gh/ExiledNarwal28/glo-2005-sportsapp)
[![Dependabot](https://badgen.net/badge/Dependabot/enabled/green?icon=dependabot)](https://dependabot.com/)

This is our project for course GLO-2005 at Laval University. We are team 8.

This project is about listing sports and practice centers. Users can recommend sports and practice centers. Sports can be practiced at different centers, depending on climate. Sports also requires specific equipment.

Our app also features a list of shops that display announces for equipment. It is built using Flask and Python.

## Installation

First, you will need [Python](https://www.python.org/downloads/).

Then, you will need to create a MySQL database. This database must fit the information displayed in [instance/flask.cfg](instance/flask.cfg).

## Prepare database

First, check that the MySQL service is well running on `localhost:3306`.

Then, in MySQL Shell (for Windows, UNIX use `mysql` CLI) : 

- `\connect --mysql root@localhost:3306`
- Enter root password
- `\sql CREATE USER 'sportsapp'@'localhost' IDENTIFIED BY 'sportsapp'`
- `\sql GRANT ALL PRIVILEGES ON *. * TO 'sportsapp'@'localhost'`
- `\sql CREATE DATABASE 'sportsapp'`
- `\sql CREATE DATABASE 'sportsapp_test'`

## Install requirements

- `pip install -q -r requirements.txt`

## Run app

- `python ./run.py`
- `python ./run.py -c` (or `--db-create` : create database tables)
- `python ./run.py -p` (or `--db-populate` : populate database with mock data)
- `python ./run.py -cp` (usually what you want)

By default, web API is hosted on port `5000` : [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Run tests

- `nose2 -v --with-coverage tests`

## Lint app and tests

- `pylint --output-format=text app`
- `pylint --output-format=text tests`
