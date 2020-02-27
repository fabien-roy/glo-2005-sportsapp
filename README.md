# GLO-2005 (H2020) - Team X

This is our project for course GLO-2005 at Laval University.

More information will be added as soon as the project is started.

## BackEnd

Our API is built using Flask and Python.

### Build and run BackEnd

Create the Dockerfile for the postgres service

- Go to `/backend/web/`
- `python create_postgres_dockerfile.py`

Build and run the Docker containers

- Go to `/backend/`
- `docker-compose build`
- `docker-compose up -d`

Create or re-initialize the database

- `docker-compose run --rm web python ./instance/db_create.py`

By default, BackEnd is hosted on port `5000` : [http://192.168.69.69:5000](http://192.168.69.69:5000).

Default address is `192.168.69.69`. Check using `docker-machine ip`.

### Test BackEnd

- Go to `/backend`
- `nose2`

For a specific module : 

- `nose2 -v project.tests.test_users`

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
