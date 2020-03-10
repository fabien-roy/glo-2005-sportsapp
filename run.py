import getopt
import sys

from flask_injector import FlaskInjector

from app import app
from app.bindings import configure
from instance.db_create import db_create
from instance.db_populate import db_populate


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "d", ["db-create"])
    except getopt.GetoptError:
        print('run.py [-d] [--db-create]')
        sys.exit()
    for opt, arg in opts:
        if opt in ("-d", "--db-create"):
            db_create()
            db_populate()  # TODO : Move in another optional argument

    FlaskInjector(app=app, modules=[configure])

    app.run()


if __name__ == "__main__":
    main(sys.argv[1:])
