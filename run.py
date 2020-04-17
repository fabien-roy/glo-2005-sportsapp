import getopt
import sys

from flask_injector import FlaskInjector

from app import app
from app.bindings import configure
from instance import db_create, db_populate
from instance.injectors import InstanceInjector

FlaskInjector(app=app, modules=[configure])

InstanceInjector(modules=[configure])


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "cp", ["db-create", "db-populate"])
    except getopt.GetoptError:
        print('run.py [-c] [--db-create]')
        print('run.py [-p] [--db-populate]')
        sys.exit()

    for opt, arg in opts:
        if opt in ("-c", "--db-create"):
            db_create()

        if opt in ("-p", "--db-populate"):
            db_populate()

    app.run()


if __name__ == "__main__":
    main(sys.argv[1:])
