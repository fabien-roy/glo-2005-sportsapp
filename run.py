import getopt
import sys

from flask_injector import FlaskInjector

from app import app
from app.bindings import configure
from app.interfaces.infrastructure.database import MySQLDatabase
from instance import Instance
from instance.modules import InstanceModule

FlaskInjector(app=app, modules=[configure])

database = MySQLDatabase()  # TODO : Wouldn't be necessary if app would create/populate db
instance = Instance(database, InstanceModule)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "cp", ["db-create", "db-populate"])
    except getopt.GetoptError:
        print('run.py [-c] [--db-create]')
        print('run.py [-p] [--db-populate]')
        sys.exit()

    for opt, arg in opts:
        if opt in ("-c", "--db-create"):
            instance.db_create()

        if opt in ("-p", "--db-populate"):
            instance.db_populate()

    app.run()


if __name__ == "__main__":
    main(sys.argv[1:])
