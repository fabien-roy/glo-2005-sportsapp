import getopt
import sys

from app import app
from instance.db_create import db_create


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "d", ["db-create"])
    except getopt.GetoptError:
        print('run.py [-d] [--db-create]')
        sys.exit()
    for opt, arg in opts:
        if opt in ("-d", "--db-create"):
            db_create()
    app.run()


if __name__ == "__main__":
    main(sys.argv[1:])
