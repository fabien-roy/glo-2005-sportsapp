# GLO-2005 (H2020) - Team X

This is our project for course GLO-2005 at Laval University.

This project is about listing sports and practice centers. Users can recommend sports and practice centers. Sports can be practiced at different centers, depending on climate. Sports also requires specific equipment.

Our app also features a list of shops that display announces for equipment. It is built using Flask and Python.

## Installation

First, you will need [Python](https://www.python.org/downloads/).

Then, you are going to need Docker. For UNIX systems, this is quite easy. For Windows, get ready to [walk through hell](https://docs.docker.com/toolbox/toolbox_install_windows/).

## Build and run

Create the Dockerfile for the mysql service

- Go to `/web/`
- `python create_mysql_dockerfile.py`

Build and run the Docker containers

- Go to `/`
- `docker-machine start default` (if Docker is not started yet)
- `docker-machine restart default` (if Docker/Windows is being picky)
- `docker-compose build`
- `docker-compose up -d`

Stop container

- Go to `/`
- `docker-compose stop`

Create or re-initialize the database

- `docker-compose run --rm web python ./instance/db_create.py`

By default, web API is hosted on port `8000` : [http://192.168.99.100:8000](http://192.168.99.100:8000).

Default address is `192.168.99.100`. Check using `docker-machine ip`.

## Run tests

- Go to `/web/`
- `pip install -q -r requirements.txt` (if needed)
- `nose2 -v --with-coverage project.tests`
