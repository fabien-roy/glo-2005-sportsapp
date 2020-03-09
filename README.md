# GLO-2005 (H2020) - Team X

This is our project for course GLO-2005 at Laval University.

This project is about listing sports and practice centers. Users can recommend sports and practice centers. Sports can be practiced at different centers, depending on climate. Sports also requires specific equipment.

Our app also features a list of shops that display announces for equipment. It is built using Flask and Python.

## Installation

First, you will need [Python](https://www.python.org/downloads/).

Then, you will need to create a MySQL database. This database must fit the information displayed in [database/flask.cfg](database/flask.cfg).

## Install requirements

- `pip install -q -r requirements.txt`

## Create database tables and mock data

- `python ./database/create_bd.py`

## Build and run

- `python ./run.py`

By default, web API is hosted on port `8000` : [http://localhost:8000](http://localhost:8000).

## Run tests

- Go to `./app/`
- `nose2 -v --with-coverage app.tests`
