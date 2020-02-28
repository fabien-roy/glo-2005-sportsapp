# GLO-2005 (H2020) - Team X

![API Unit tests](https://github.com/ExiledNarwal28/glo-2005-project/workflows/API%20Unit%20tests/badge.svg)

This is our project for course GLO-2005 at Laval University.

More information will be added as soon as the project is started.

## BackEnd

Our API is built using Flask and Python.

### Installation

First, you will need [Python](https://www.python.org/downloads/).

Then, you are going to need Docker. For UNIX systems, this is quite easy. For Windows, get ready to [walk through hell](https://docs.docker.com/docker-for-windows/install/).

### Build and run BackEnd

Create the Dockerfile for the mysql service

- Go to `/backend/web/`
- `python create_mysql_dockerfile.py`

Build and run the Docker containers

- Go to `/backend/`
- `docker-machine start default` (if Docker is not started yet)
- `docker-machine restart default` (if Docker/Windows is being picky)
- `docker-compose build`
- `docker-compose up -d`

Stop container

- Go to `/backend/`
- `docker-compose stop`

Create or re-initialize the database

- `docker-compose run --rm web python ./instance/db_create.py`

By default, web API is hosted on port `8000` : [http://192.168.99.100:8000](http://192.168.99.100:8000).

Default address is `192.168.99.100`. Check using `docker-machine ip`.

### Test BackEnd

- Go to `/backend/web`
- `pip install -q -r requirements.txt` (if needed)
- `nose2 -v --with-coverage project.tests`

## FrontEnd

Our FrontEnd is built using Vue.js.

### Build FrontEnd

`npm build`

### Run FrontEnd

`npm start`

By default, FrontEnd is hosted on port `8080` : [http://localhost.com:8080](http://localhost.com:8080).

### Test FrontEnd

`npm test`

### Check FrontEnd code style

`npm lint`
