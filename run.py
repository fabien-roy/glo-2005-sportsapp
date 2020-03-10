from app import app
from instance.db_create import db_create

# TODO : Only if there is an argument (like --db-create)
db_create()

if __name__ == "__main__":
    app.run()
